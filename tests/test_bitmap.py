import context
from io import BytesIO
from ard.bitmap import Bitmap
from ard.color import Color


class TestBimap:
    def test_writes_magic_header(self):
        view = self.empty_image_view()
        assert view[0] == 0x42
        assert view[1] == 0x4d

    def test_writes_file_header(self):
        view = self.empty_image_view()
        assert view[2] == 14+40+4
        assert view[3] == 0
        assert view[4] == 0
        assert view[5] == 0
        assert view[6] == 0
        assert view[7] == 0
        assert view[8] == 0
        assert view[9] == 0
        assert view[10] == 14+40
        assert view[11] == 0
        assert view[12] == 0
        assert view[13] == 0

    def test_write_info_header(self):
        view = self.empty_image_view()
        assert view[14:18] == b'\x28\x00\x00\x00'
        assert view[18:22] == b'\x01\x00\x00\x00'
        assert view[22:26] == b'\x01\x00\x00\x00'
        assert view[26:28] == b'\x01\x00'
        assert view[28:30] == b'\x18\x00'
        assert view[30:34] == b'\x00\x00\x00\x00'
        assert view[34:38] == b'\x04\x00\x00\x00'
        assert view[38:42] == b'\x00\x00\x00\x00'
        assert view[42:46] == b'\x00\x00\x00\x00'
        assert view[46:50] == b'\x00\x00\x00\x00'
        assert view[50:54] == b'\x00\x00\x00\x00'

    def test_write_pixels_with_padding(self):
        view = self.empty_image_view()
        assert view.nbytes == 58
        assert view[54:58] == b'\x00\x00\xff\x00'

    def empty_image_view(self):
        stream = BytesIO()
        bitmap = Bitmap(width=1, height=1, colors=[Color(1, 0, 0)])
        bitmap.write_to(stream)
        return stream.getbuffer()
