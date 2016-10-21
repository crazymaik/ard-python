import context
from ard.color import Color


class TestColor:
    def test_clamp_example(self):
        actual = Color(r=-0.0001, g=0.5, b=1.0001).clamp()
        assert actual.r == 0.0
        assert actual.g == 0.5
        assert actual.b == 1.0

    def test_add_example(self):
        c0 = Color(r=0, g=1, b=2)
        c1 = Color(r=3, g=4, b=5)
        actual = c0 + c1
        assert actual.r == 3
        assert actual.g == 5
        assert actual.b == 7

    def test_div_example(self):
        c = Color(r=1, g=2, b=4)
        actual = c.div(2)
        assert actual.r == 0.5
        assert actual.g == 1
        assert actual.b == 2
