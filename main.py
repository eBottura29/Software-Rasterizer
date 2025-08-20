import os
import random

from classes import CubeModel, RenderTarget, float3
from parsers import obj_parser
from renderer import render


# old code for creating a test image, commented out
# def create_test_image(img):
#     a = float2(0.2 * img.width, 0.2 * img.height)
#     b = float2(0.7 * img.width, 0.4 * img.height)
#     c = float2(0.4 * img.width, 0.8 * img.height)

#     for y in range(img.height):
#         for x in range(img.width):
#             inside = maths.point_in_triangle(tri2(a, b, c), float2(x, y))

#             if inside:
#                 img.image[x][y] = float3(x=255, y=255, z=255)

#     return img


def main():
    obj_path = os.getcwd() + "\\obj\\cube.obj"
    print(f"Loading OBJ file from: {obj_path}")
    cube_model_vertices = obj_parser(obj_path)

    triangle_cols = [
        float3(x=random.randint(0, 255), y=random.randint(0, 255), z=random.randint(0, 255)) for _ in range(len(cube_model_vertices) // 3)
    ]

    cube_model = CubeModel(cube_model_vertices, triangle_cols)
    render_target = RenderTarget(w=64, h=64, background_color=float3(0, 0, 0))

    render(cube_model, render_target)


if __name__ == "__main__":
    main()
