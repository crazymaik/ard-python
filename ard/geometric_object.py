from ard.color import Color
from ard.ray import Ray
from ard.vector3 import Vector3
from typing import Optional


class ShadeRecord:
    def __init__(self, hit_point: Vector3, normal: Vector3, color: Color) -> None:
        self._hit_point = hit_point
        self._normal = normal
        self._color = color

    @property
    def hit_point(self) -> Vector3:
        return self._hit_point

    @property
    def normal(self) -> Vector3:
        return self._normal

    @property
    def color(self) -> Color:
        return self._color


class HitResult:
    def __init__(self, tmin: float, shade_record: ShadeRecord) -> None:
        self._tmin = tmin
        self._shade_record = shade_record

    @property
    def tmin(self) -> float:
        return self._tmin

    @property
    def shade_record(self) -> ShadeRecord:
        return self._shade_record


class GeometricObject:
    def hit(self, ray: Ray) -> Optional[HitResult]:
        return NotImplemented
