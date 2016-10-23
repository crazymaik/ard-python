import math


class Vector3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self) -> float:
        return self._z

    def add(self, other: Vector3) -> Vector3:
        return Vector3(x=self.x + other.x,
                       y=self.y + other.y,
                       z=self.z + other.z)

    def __add__(self, other: Vector3) -> Vector3:
        return self.add(other)

    def sub(self, other: Vector3) -> Vector3:
        return Vector3(x=self.x - other.x,
                       y=self.y - other.y,
                       z=self.z - other.z)

    def __sub__(self, other: Vector3) -> Vector3:
        return self.sub(other)

    def mul(self, value: float) -> Vector3:
        return Vector3(x=self.x * value,
                       y=self.y * value,
                       z=self.z * value)

    def div(self, value: float) -> Vector3:
        reciprocal = 1.0 / value
        return Vector3(x=self.x * reciprocal,
                       y=self.y * reciprocal,
                       z=self.z * reciprocal)

    def length_squared(self) -> float:
        return self.x*self.x + self.y*self.y + self.z*self.z

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def dot(self, other: Vector3) -> float:
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other: Vector3) -> Vector3:
        return Vector3(self.y*other.z - self.z*other.y,
                       self.z*other.x - self.x*other.z,
                       self.x*other.y - self.y*other.x)

    def normalized(self) -> Vector3:
        reciprocal = 1.0 / self.length()
        return self.mul(reciprocal)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
