from ard.color import Color
from ard.geometric_object import GeometricObject
from ard.ray import Ray
from ard.tracer import Tracer
from ard.vector3 import Vector3
from ard.view_plane import ViewPlane


class World:

    def __init__(self, view_plane, background_color, tracer, scene_objects):
        self._view_plane = view_plane
        self._background_color = background_color
        self._tracer = tracer
        self._scene_objects = scene_objects

    @property
    def background_color(self):
        return self._background_color

    @property
    def scene_objects(self):
        return self._scene_objects

    def render(self):
        hres = self._view_plane.horizontal_resolution
        vres = self._view_plane.vertical_resolution
        pixel_size = self._view_plane.pixel_size
        colors = [None] * (hres*vres)

        for r in range(vres):
            for c in range(hres):
                x = pixel_size * (c - 0.5 * (hres - 1.0))
                y = pixel_size * (r - 0.5 * (vres - 1.0))
                ray = Ray(origin=Vector3(x=x, y=y, z=100),
                          direction=Vector3(x=0, y=0, z=-1))
                color = self._tracer.trace_ray(ray, self)
                colors[r * hres + c] = color

        return colors
