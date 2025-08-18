from tris import tri2
from floats import float2


def dot(a: float2, b: float2):
    return a.x * b.x + a.y * b.y


def perpendicular(vec: float2):
    return float2(vec.y, -vec.x)


def point_on_right_side_of_line(a: float2, b: float2, p: float2):
    ap = float2(p.x - a.x, p.y - a.y)
    ab_perp = perpendicular(float2(b.x - a.x, b.y - a.y))
    return True if dot(ap, ab_perp) >= 0 else False


def point_in_triangle(tri: tri2, p: float2):
    side_ab = point_on_right_side_of_line(tri.a, tri.b, p)
    side_bc = point_on_right_side_of_line(tri.b, tri.c, p)
    side_ca = point_on_right_side_of_line(tri.c, tri.a, p)
    return side_ab == side_bc and side_bc == side_ca
