
class Color:
    @classmethod
    def from_color(cls, other: Color) -> Color:
        return Color(r=other.r, g=other.g, b=other.b)

    def __init__(self, r: float, g: float, b: float) -> None:
        self._r = r
        self._g = g
        self._b = b

    @property
    def r(self) -> float:
        return self._r

    @property
    def g(self) -> float:
        return self._g

    @property
    def b(self) -> float:
        return self._b

    def add(self, other: Color) -> Color:
        return Color(r=self.r + other.r,
                     g=self.g + other.g,
                     b=self.b + other.b)

    def __add__(self, other: Color) -> Color:
        return self.add(other)

    def mul(self, value: float) -> Color:
        return Color(r=self.r*value,
                     g=self.g*value,
                     b=self.b*value)

    def div(self, value: float) -> Color:
        reciprocal = 1.0 / value
        return self.mul(reciprocal)

    def clamp(self) -> Color:
        def f(d):
            return min(1, max(0, d))
        return Color(r=f(self.r), g=f(self.g), b=f(self.b))
