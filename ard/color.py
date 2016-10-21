
class Color:
    @classmethod
    def from_color(cls, other):
        return Color(r=other.r, g=other.g, b=other.b)

    def __init__(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    def clamp(self):
        def f(d):
            return min(1, max(0, d))
        return Color(r=f(self.r), g=f(self.g), b=f(self.b))
