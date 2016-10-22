import random
import sys

from ard.bitmap import Bitmap
from ard.color import Color
from ard.sampler import StandardSampler, JitteredSampler
from ard.sphere import Sphere
from ard.tracer import Tracer
from ard.vector3 import Vector3
from ard.view_plane import ViewPlane
from ard.world import World


def main():
    print("Rendering...")

    width = 160
    height = 120

    world = World(
        view_plane=ViewPlane(
            hres=width,
            vres=height,
            pixel_size=0.5,
            gamma=1.0,
            # sampler=StandardSampler()),
            sampler=JitteredSampler(
                samples_per_axis=3,
                num_sets=1,
                random=random)),
        background_color=Color(r=0, g=0, b=0),
        tracer=Tracer(),
        scene_objects=[
            Sphere(
                center=Vector3(x=-100, y=0, z=0),
                radius=70.0,
                color=Color(r=1, g=0, b=0)),
            Sphere(
                center=Vector3(x=00, y=0, z=0),
                radius=25.0,
                color=Color(r=0, g=1, b=0)),
            Sphere(
                center=Vector3(x=100, y=0, z=0),
                radius=70.0,
                color=Color(r=0, g=0, b=1))
        ]
    )

    colors = world.render()
    bitmap = Bitmap(width=width, height=height, colors=colors)
    with open("out.bmp", "wb") as file:
        bitmap.write_to(file)

    print("Done")

if __name__ == "__main__":
    main()
