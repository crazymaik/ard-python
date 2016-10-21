import context
from ard.color import Color
from ard.geometric_object import GeometricObject, HitResult, ShadeRecord
from ard.ray import Ray
from ard.sphere import Sphere
from ard.vector3 import Vector3


class TestSphere:
    def test_hit_example(self):
        color = Color(r=0, g=0, b=0)
        ray = Ray(origin=Vector3(x=0, y=0, z=0),
                  direction=Vector3(x=1, y=0, z=0))
        sphere = Sphere(center=Vector3(x=2, y=0, z=0), radius=1, color=color)
        result = sphere.hit(ray)
        assert result is not None
        assert result.shade_record.hit_point == Vector3(x=1, y=0, z=0)
        assert result.tmin == 1

    def test_not_hit_example(self):
        color = Color(r=0, g=0, b=0)
        ray = Ray(origin=Vector3(x=0, y=0, z=0),
                  direction=Vector3(x=1, y=1, z=0))
        sphere = Sphere(center=Vector3(x=2, y=0, z=0), radius=1, color=color)
        result = sphere.hit(ray)
        assert result is None

    def test_hit_inside_positive_direction(self):
        color = Color(r=0, g=0, b=0)
        ray = Ray(origin=Vector3(x=1, y=0, z=0),
                  direction=Vector3(x=1, y=0, z=0))
        sphere = Sphere(center=Vector3(x=1, y=0, z=0), radius=2, color=color)
        result = sphere.hit(ray)
        assert result is not None
        assert result.shade_record.hit_point == Vector3(x=3, y=0, z=0)
        assert result.tmin == 2

    def test_hit_inside_negative_direction(self):
        color = Color(r=0, g=0, b=0)
        ray = Ray(origin=Vector3(x=1, y=0, z=0),
                  direction=Vector3(x=-1, y=0, z=0))
        sphere = Sphere(center=Vector3(x=1, y=0, z=0), radius=2, color=color)
        result = sphere.hit(ray)
        assert result is not None
        assert result.shade_record.hit_point == Vector3(x=-1, y=0, z=0)
        assert result.tmin == 2
