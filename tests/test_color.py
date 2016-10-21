import context
from ard.color import Color


class TestColor:
    def test_clamp_example(self):
        actual = Color(r=-0.0001, g=0.5, b=1.0001).clamp()
        assert actual.r == 0.0
        assert actual.g == 0.5
        assert actual.b == 1.0
