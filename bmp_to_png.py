# this script is standalone

import os
import struct
import zlib
from pathlib import Path


class Inputs:
    directory = r"C:\Users\ricob\Desktop\Programming\Python\Software Rasterizer\renders\first_animation"


class BMP2PNGConverter:
    def __init__(self, in_dir: str):
        self.in_dir = Path(in_dir)
        self.out_dir = self.in_dir / "png"
        self.out_dir.mkdir(exist_ok=True)

    def convert_all(self):
        bmp_files = list(self.in_dir.glob("*.bmp"))
        if not bmp_files:
            print("No BMP files found in", self.in_dir)
            return

        for bmp in bmp_files:
            try:
                out_file = self.out_dir / (bmp.stem + ".png")
                self.bmp_to_png(bmp, out_file)
                print(f"Converted: {bmp} -> {out_file}")
            except Exception as e:
                print(f"Error converting {bmp}: {e}")

    def bmp_to_png(self, in_path: Path, out_path: Path):
        with open(in_path, "rb") as f:
            bmp = f.read()

        # --- Parse BMP header ---
        file_type = bmp[0:2]
        if file_type != b"BM":
            raise ValueError("Not a BMP file")

        pixel_offset = struct.unpack_from("<I", bmp, 10)[0]
        header_size = struct.unpack_from("<I", bmp, 14)[0]
        width = struct.unpack_from("<I", bmp, 18)[0]
        height = struct.unpack_from("<I", bmp, 22)[0]
        planes = struct.unpack_from("<H", bmp, 26)[0]
        bpp = struct.unpack_from("<H", bmp, 28)[0]
        compression = struct.unpack_from("<I", bmp, 30)[0]

        if planes != 1 or compression != 0:
            raise NotImplementedError("Only uncompressed BMPs are supported")

        if bpp not in (24, 32):
            raise NotImplementedError("Only 24-bit and 32-bit BMP supported")

        row_padded = ((width * (bpp // 8) + 3) // 4) * 4
        pixels = []
        for y in range(height):
            row_start = pixel_offset + y * row_padded
            row = []
            for x in range(width):
                if bpp == 24:
                    b, g, r = struct.unpack_from("BBB", bmp, row_start + x * 3)
                    row.extend([r, g, b])
                elif bpp == 32:
                    b, g, r, a = struct.unpack_from("BBBB", bmp, row_start + x * 4)
                    row.extend([r, g, b, a])
            pixels.insert(0, row)  # BMP rows are bottom-up

        # --- Write PNG ---
        def png_chunk(chunk_type, data):
            chunk = struct.pack("!I", len(data))
            chunk += chunk_type
            chunk += data
            crc = zlib.crc32(chunk_type + data) & 0xFFFFFFFF
            chunk += struct.pack("!I", crc)
            return chunk

        color_type = 2 if bpp == 24 else 6
        bit_depth = 8

        raw_data = b""
        for row in pixels:
            raw_data += b"\x00" + bytes(row)  # no filter

        compressed = zlib.compress(raw_data, 9)

        png = b"\x89PNG\r\n\x1a\n"
        png += png_chunk(b"IHDR", struct.pack("!IIBBBBB", width, height, bit_depth, color_type, 0, 0, 0))
        png += png_chunk(b"IDAT", compressed)
        png += png_chunk(b"IEND", b"")

        with open(out_path, "wb") as f:
            f.write(png)


if __name__ == "__main__":
    conv = BMP2PNGConverter(Inputs.directory)
    conv.convert_all()
