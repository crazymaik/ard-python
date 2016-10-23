from ard.color import Color
from ard.geometric_object import GeometricObject
from ard.ray import Ray
from ard.tracer import Tracer
from ard.vector3 import Vector3
from ard.view_plane import ViewPlane


class World:

    def __init__(self, view_plane: ViewPlane, background_color: Color,
                 tracer: Tracer, scene_objects: List[GeometricObject]) -> None:
        self._view_plane = view_plane
        self._background_color = background_color
        self._tracer = tracer
        self._scene_objects = scene_objects

    @property
    def background_color(self) -> Color:
        return self._background_color

    @property
    def scene_objects(self) -> List[GeometricObject]:
        return self._scene_objects

    def render(self) -> List[Color]:
        hres = self._view_plane.horizontal_resolution
        vres = self._view_plane.vertical_resolution
        pixel_size = self._view_plane.pixel_size
        colors = [None] * (hres*vres)  # type: List[Color]
        num_samples = self._view_plane.sampler.num_samples

        for r in range(vres):
            for c in range(hres):
                color = Color(r=0, g=0, b=0)
                samples = self._view_plane.sampler.sample_unit_square(0)
                for i in range(num_samples):
                    x = pixel_size * (c - 0.5 * hres + samples[i].x)
                    y = pixel_size * (r - 0.5 * vres + samples[i].y)
                    ray = Ray(origin=Vector3(x=x, y=y, z=100),
                              direction=Vector3(x=0, y=0, z=-1))
                    color += self._tracer.trace_ray(ray, self)
                colors[r * hres + c] = color.div(num_samples)

        return colors
