import math

from bmp import write_to_bmp
import maths
from classes import tri2, float2


def render(model, target):
    print(f"Rendering model with {len(model.vertices) // 3} triangles to target of size {target.width}x{target.height}")
    for i in range(0, len(model.vertices), 3):
        a = maths.world_to_screen(model.vertices[i + 0], model.transform, target.size)
        b = maths.world_to_screen(model.vertices[i + 1], model.transform, target.size)
        c = maths.world_to_screen(model.vertices[i + 2], model.transform, target.size)

        min_x = min(a.x, b.x, c.x)
        min_y = min(a.y, b.y, c.y)
        max_x = max(a.x, b.x, c.x)
        max_y = max(a.y, b.y, c.y)

        block_start_x = maths.clamp(int(min_x), 0, target.width - 1)
        block_start_y = maths.clamp(int(min_y), 0, target.height - 1)
        block_end_x = maths.clamp(int(max_x), 0, target.width - 1)
        block_end_y = maths.clamp(int(max_y), 0, target.height - 1)

        for y in range(block_start_y, block_end_y + 1):
            for x in range(block_start_x, block_end_x + 1):
                if maths.point_in_triangle(tri2(a, b, c), float2(x, y)):
                    target.color_buffer[x][y] = model.cols[i // 3]

        write_to_bmp(target)
