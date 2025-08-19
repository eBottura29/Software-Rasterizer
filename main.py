from image import Image
from image import write_to_bmp
from floats import float2, float3
import maths
from tris import tri2


def create_test_image(img):
    a = float2(0.2 * img.width, 0.2 * img.height)
    b = float2(0.7 * img.width, 0.4 * img.height)
    c = float2(0.4 * img.width, 0.8 * img.height)

    for y in range(img.height):
        for x in range(img.width):
            inside = maths.point_in_triangle(tri2(a, b, c), float2(x, y))

            if inside:
                img.image[x][y] = float3(x=255, y=255, z=255)

    return img


def render(img):
    write_to_bmp(img)


def main(img):
    img_final = create_test_image(img)
    render(img_final)


if __name__ == "__main__":
    img = Image(size=float2(x=64, y=64), background_color=float3(x=0, y=0, z=0))
    main(img)
