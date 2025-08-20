class float2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class float3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.r = x
        self.g = y
        self.b = z


class tri2:
    def __init__(self, a=float2, b=float2, c=float2):
        self.a = a
        self.b = b
        self.c = c


class RenderTarget:
    def __init__(self, w, h, background_color=float3(0, 0, 0)):
        self.color_buffer = [[background_color for _ in range(h)] for _ in range(w)]

        self.width = w
        self.height = h
        self.size = float2(w, h)


class CubeModel:
    def __init__(self, vertices, cols):
        self.vertices = vertices
        self.cols = cols
