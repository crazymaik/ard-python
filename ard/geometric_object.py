
class ShadeRecord:
    def __init__(self, hit_point, normal, color):
        self._hit_point = hit_point
        self._normal = normal
        self._color = color

    @property
    def hit_point(self):
        return self._hit_point

    @property
    def normal(self):
        return self._normal

    @property
    def color(self):
        return self._color


class HitResult:
    def __init__(self, tmin, shade_record):
        self._tmin = tmin
        self._shade_record = shade_record

    @property
    def tmin(self):
        return self._tmin

    @property
    def shade_record(self):
        return self._shade_record


class GeometricObject:
    def hit(ray):
        return NotImplemented
