import context
from ard.ray import Ray
from ard.vector3 import Vector3


class TestRay:
    def test_from_ray_example(self):
        r0 = Ray(origin=Vector3(x=1, y=2, z=3),
                 direction=Vector3(x=1, y=0, z=0))
        other = Ray.from_ray(r0)
        assert other.origin == Vector3(x=1, y=2, z=3)
        assert other.direction == Vector3(x=1, y=0, z=0)
