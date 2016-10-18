import context
from ard.bitmap import Bitmap

def test_assert_bitmap_test_returns_1():
    bm = Bitmap()
    assert bm.test() == 1

