import os, random, time
from datetime import datetime

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


def load_model():
    obj_path = os.getcwd() + "\\obj\\cube.obj"
    print(f"Loading OBJ file from: {obj_path}")
    cube_model_vertices = obj_parser(obj_string=open(obj_path, "r").read())

    triangle_cols = [
        float3(x=random.randint(0, 255), y=random.randint(0, 255), z=random.randint(0, 255)) for _ in range(len(cube_model_vertices) // 3)
    ]

    cube_model = CubeModel(cube_model_vertices, triangle_cols)
    render_target = RenderTarget(w=256, h=256, background_color=float3(0, 0, 0))

    return cube_model, render_target


def render_animation(frame_count=30):
    cube_model, render_target = load_model()

    print(f"Rendering an animation")
    print(f"Rendering {frame_count} frames...")

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out_dir = os.path.join(os.getcwd(), "renders", now)
    os.makedirs(out_dir, exist_ok=True)

    for frame in range(frame_count):
        start = time.time()

        render_target.color_buffer = [[float3(0, 0, 0) for _ in range(render_target.height)] for _ in range(render_target.width)]
        cube_model.transform.yaw += 10.0
        render(cube_model, render_target, True, frame + 1, out_dir)

        end = time.time()

        print(f"Frame {frame + 1}/{frame_count} rendered in {(end - start)*1000:.2f} ms")


def render_image():
    cube_model, render_target = load_model()

    print("Rendering an image...")

    render(cube_model, render_target)


def main():
    render_animation()


if __name__ == "__main__":
    main()
