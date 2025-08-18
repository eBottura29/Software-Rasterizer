import os
import struct
from datetime import datetime
from floats import float2, float3


class Image:
    def __init__(self, size: float2 = float2(x=64, y=64), background_color: float3 = float3(x=0, y=0, z=0)):
        self.width = size.x
        self.height = size.y

        # Create image list - self.image[x][y]
        self.image = [[background_color for _ in range(self.height)] for _ in range(self.width)]


def write_to_bmp(img: Image):
    width, height = int(img.width), int(img.height)

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
            pixel = img.image[x][y]
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
