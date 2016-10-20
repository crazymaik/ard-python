import sys

from ard.bitmap import Bitmap, Color


def main():
    colors = []
    for y in range(768):
        for x in range(1024):
            colors.append(Color(x % 256 / 255, y % 256 / 255, 0))
    bitmap = Bitmap(width=1024, height=768, colors=colors)
    with open("out.bmp", "wb") as file:
        bitmap.write_to(file)

if __name__ == "__main__":
    main()
