from math import sin, cos


class float2:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f"float2(x={self.x}, y={self.y})"

    # Equality & comparison
    def __eq__(self, other):
        if isinstance(other, float2):
            return (self.x, self.y) == (other.x, other.y)
        return False

    # Addition
    def __add__(self, other):
        if isinstance(other, float2):
            return float2(self.x + other.x, self.y + other.y)
        return float2(self.x + other, self.y + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, float2):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, float2):
            return float2(self.x - other.x, self.y - other.y)
        return float2(self.x - other, self.y - other)

    def __rsub__(self, other):
        if isinstance(other, float2):
            return float2(other.x - self.x, other.y - self.y)
        return float2(other - self.x, other - self.y)

    def __isub__(self, other):
        if isinstance(other, float2):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self

    # Multiplication (scalar or component-wise)
    def __mul__(self, other):
        if isinstance(other, float2):
            return float2(self.x * other.x, self.y * other.y)
        return float2(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, float2):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self

    # Division
    def __truediv__(self, other):
        if isinstance(other, float2):
            return float2(self.x / other.x, self.y / other.y)
        return float2(self.x / other, self.y / other)

    def __rtruediv__(self, other):
        if isinstance(other, float2):
            return float2(other.x / self.x, other.y / self.y)
        return float2(other / self.x, other / self.y)

    def __itruediv__(self, other):
        if isinstance(other, float2):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other
        return self

    # Negation
    def __neg__(self):
        return float2(-self.x, -self.y)

    # Absolute value
    def __abs__(self):
        return float2(abs(self.x), abs(self.y))

    # Length (for truthiness)
    def __len__(self):
        return 2

    def __iter__(self):
        return iter((self.x, self.y))

    def __getitem__(self, index):
        return (self.x, self.y)[index]

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")


class float3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        # alias for RGB use
        self.r = self.x
        self.g = self.y
        self.b = self.z

    def __repr__(self):
        return f"float3(x={self.x}, y={self.y}, z={self.z})"

    # Equality & comparison
    def __eq__(self, other):
        if isinstance(other, float3):
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        return False

    # Addition
    def __add__(self, other):
        if isinstance(other, float3):
            return float3(self.x + other.x, self.y + other.y, self.z + other.z)
        return float3(self.x + other, self.y + other, self.z + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, float3):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            self.x += other
            self.y += other
            self.z += other
        return self

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, float3):
            return float3(self.x - other.x, self.y - other.y, self.z - other.z)
        return float3(self.x - other, self.y - other, self.z - other)

    def __rsub__(self, other):
        if isinstance(other, float3):
            return float3(other.x - self.x, other.y - self.y, other.z - self.z)
        return float3(other - self.x, other - self.y, other - self.z)

    def __isub__(self, other):
        if isinstance(other, float3):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            self.x -= other
            self.y -= other
            self.z -= other
        return self

    # Multiplication (scalar or component-wise)
    def __mul__(self, other):
        if isinstance(other, float3):
            return float3(self.x * other.x, self.y * other.y, self.z * other.z)
        return float3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if isinstance(other, float3):
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        else:
            self.x *= other
            self.y *= other
            self.z *= other
        return self

    # Division
    def __truediv__(self, other):
        if isinstance(other, float3):
            return float3(self.x / other.x, self.y / other.y, self.z / other.z)
        return float3(self.x / other, self.y / other, self.z / other)

    def __rtruediv__(self, other):
        if isinstance(other, float3):
            return float3(other.x / self.x, other.y / self.y, other.z / self.z)
        return float3(other / self.x, other / self.y, other / self.z)

    def __itruediv__(self, other):
        if isinstance(other, float3):
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        else:
            self.x /= other
            self.y /= other
            self.z /= other
        return self

    # Negation
    def __neg__(self):
        return float3(-self.x, -self.y, -self.z)

    # Absolute value
    def __abs__(self):
        return float3(abs(self.x), abs(self.y), abs(self.z))

    # Length (for truthiness)
    def __len__(self):
        return 3

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __getitem__(self, index):
        return (self.x, self.y, self.z)[index]

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index out of range")


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


class Transform:
    def __init__(self, pitch=0.0, roll=0.0, yaw=0.0):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def to_world_vertex(self, vertex: float3):
        ihat, jhat, khat = self.get_basis_vectors()
        return self.transform_vector(ihat, jhat, khat, vertex)

    def get_basis_vectors(self):
        # YAW
        ihat_yaw = float3(cos(self.yaw), 0, sin(self.yaw))
        jhat_yaw = float3(0, 1, 0)
        khat_yaw = float3(-sin(self.yaw), 0, cos(self.yaw))

        # PITCH
        ihat_pitch = float3(1, 0, 0)
        jhat_pitch = float3(0, cos(self.pitch), sin(self.pitch))
        khat_pitch = float3(0, -sin(self.pitch), cos(self.pitch))

        # ROLL
        ihat_roll = float3(cos(self.roll), sin(self.roll), 0)
        jhat_roll = float3(-sin(self.roll), cos(self.roll), 0)
        khat_roll = float3(0, 0, 1)

        # Combine transformations (Yaw → Pitch → Roll)
        ihat = self.transform_vector(ihat_yaw, jhat_yaw, khat_yaw, self.transform_vector(ihat_pitch, jhat_pitch, khat_pitch, ihat_roll))
        jhat = self.transform_vector(ihat_yaw, jhat_yaw, khat_yaw, self.transform_vector(ihat_pitch, jhat_pitch, khat_pitch, jhat_roll))
        khat = self.transform_vector(ihat_yaw, jhat_yaw, khat_yaw, self.transform_vector(ihat_pitch, jhat_pitch, khat_pitch, khat_roll))

        return ihat, jhat, khat

    @staticmethod
    def transform_vector(ihat, jhat, khat, vector):
        return vector.x * ihat + vector.y * jhat + vector.z * khat


class CubeModel:
    def __init__(self, vertices, cols):
        self.vertices = vertices
        self.cols = cols

        self.transform = Transform(pitch=20.0, roll=0.0, yaw=20.0)
