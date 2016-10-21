from ard.vector3 import Vector3


class Ray:
    @classmethod
    def from_ray(cls, other):
        return Ray(origin=other.origin, direction=other.direction)

    def __init__(self, origin, direction):
        self._origin = origin
        self._direction = direction

    @property
    def origin(self):
        return self._origin

    @property
    def direction(self):
        return self._direction
