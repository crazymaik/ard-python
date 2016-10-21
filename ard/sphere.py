import math
from ard.ray import Ray
from ard.geometric_object import GeometricObject, HitResult, ShadeRecord


class Sphere:
    def __init__(self, center, radius, color):
        self._center = center
        self._radius = radius
        self._color = color

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    @property
    def color(self):
        return self._color

    def hit(self, ray):
        temp = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * temp.dot(ray.direction)
        c = temp.dot(temp) - self.radius * self.radius
        disc = b*b - 4.0*a*c

        if disc >= 0.0:

            def calc_result(t):
                normal = (temp + ray.direction.mul(t)).div(self.radius)
                hit_point = ray.origin + ray.direction.mul(t)
                sr = ShadeRecord(hit_point=hit_point,
                                 normal=normal,
                                 color=self.color)
                return HitResult(tmin=t,
                                 shade_record=sr)

            e = math.sqrt(disc)
            denom = 2*a
            t = (-b - e) / denom

            if t > 0.00001:
                return calc_result(t)

            t = (-b + e) / denom

            if t > 0.00001:
                return calc_result(t)

        return None
