import os
import struct
from datetime import datetime
from classes import RenderTarget


# written by AI, couldnt be bothered to write it myself
def write_to_bmp(tgt: RenderTarget):
    width, height = int(tgt.width), int(tgt.height)

    # Each row must be padded to a multiple of 4 bytes
    row_bytes = width * 3
    padding = (4 - (row_bytes % 4)) % 4
    row_size = row_bytes + padding

    # File size = headers (14+40) + pixel data
    pixel_data_size = row_size * height
    file_size = 14 + 40 + pixel_data_size

    # --- BMP Header (14 bytes) ---
    bmp_header = struct.pack("<2sIHHI", b"BM", file_size, 0, 0, 54)  # Signature  # File size  # Reserved  # Offset to pixel data (14+40)

    # --- DIB Header (40 bytes: BITMAPINFOHEADER) ---
    dib_header = struct.pack(
        "<IIIHHIIIIII",
        40,  # Header size
        width,
        height,
        1,  # Color planes
        24,  # Bits per pixel
        0,  # Compression (none)
        pixel_data_size,
        2835,  # Horizontal resolution (72 DPI)
        2835,  # Vertical resolution
        0,  # Colors in palette
        0,  # Important colors
    )

    # --- Pixel Data ---
    pixel_bytes = bytearray()
    for y in range(height - 1, -1, -1):  # bottom to top
        for x in range(width):
            pixel = tgt.image[x][y]
            # BMP is BGR
            pixel_bytes.extend([int(pixel.b) & 0xFF, int(pixel.g) & 0xFF, int(pixel.r) & 0xFF])
        # Add padding
        pixel_bytes.extend(b"\x00" * padding)

    # Combine everything
    bmp_data = bmp_header + dib_header + pixel_bytes

    # --- Save to file ---
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out_dir = os.path.join(os.getcwd(), "renders", now)
    os.makedirs(out_dir, exist_ok=True)

    file_path = os.path.join(out_dir, "image.bmp")
    with open(file_path, "wb") as f:
        f.write(bmp_data)

    return file_path
