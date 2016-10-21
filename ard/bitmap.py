import math
import struct
from collections import namedtuple


class Bitmap:
    def __init__(self, width, height, colors):
        self.width = width
        self.height = height
        self.colors = colors
        self.row_padding = (4 - (width*3 % 4)) % 4
        self.row_size = width*3 + self.row_padding
        return

    def write_to(self, stream):
        self.write_file_header(stream)
        self.write_info_header(stream)
        self.write_pixels(stream)

    def write_file_header(self, stream):
        stream.write(b'\x42\x4d')
        filesize = 14 + 40 + self.row_size * self.height
        stream.write(struct.pack('<I', filesize))
        stream.write(struct.pack('<H', 0))
        stream.write(struct.pack('<H', 0))
        stream.write(struct.pack('<I', 14 + 40))

    def write_info_header(self, stream):
        stream.write(struct.pack('<I', 40))
        stream.write(struct.pack('<I', self.width))
        stream.write(struct.pack('<I', self.height))
        stream.write(struct.pack('<H', 1))
        stream.write(struct.pack('<H', 24))
        stream.write(struct.pack('<I', 0))
        stream.write(struct.pack('<I', self.row_size * self.height))
        stream.write(struct.pack('<I', 0))
        stream.write(struct.pack('<I', 0))
        stream.write(struct.pack('<I', 0))
        stream.write(struct.pack('<I', 0))

    def write_pixels(self, stream):
        for y in range(self.height):
            for x in range(self.width):
                color = self.colors[y * self.width + x]
                stream.write(struct.pack('B', int(round(color.b * 255))))
                stream.write(struct.pack('B', int(round(color.g * 255))))
                stream.write(struct.pack('B', int(round(color.r * 255))))
            if self.row_padding >= 3:
                stream.write(b'\x00')
            if self.row_padding >= 2:
                stream.write(b'\x00')
            if self.row_padding >= 1:
                stream.write(b'\x00')
