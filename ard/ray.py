from ard.vector3 import Vector3


class Ray:
    @classmethod
    def from_ray(cls, other: Ray) -> Ray:
        return Ray(origin=other.origin, direction=other.direction)

    def __init__(self, origin: Vector3, direction: Vector3) -> None:
        self._origin = origin
        self._direction = direction

    @property
    def origin(self) -> Vector3:
        return self._origin

    @property
    def direction(self) -> Vector3:
        return self._direction
