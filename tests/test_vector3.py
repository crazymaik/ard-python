import context
import math
import pytest
from ard.vector3 import Vector3


class TestVector3:
    def test_add_example(self):
        u = Vector3(x=1, y=2, z=3)
        v = Vector3(x=4, y=5, z=6)
        actual = u.add(v)
        assert actual.x == 5
        assert actual.y == 7
        assert actual.z == 9

    def test_add_and_sub_equalize(self):
        u = Vector3(x=1, y=2, z=3)
        v = Vector3(x=4, y=5, z=6)
        actual = u.add(v).sub(v)
        assert actual.x == u.x
        assert actual.y == u.y
        assert actual.z == u.z

    def test_add_and_sub_operators(self):
        u = Vector3(x=1, y=2, z=3)
        v = Vector3(x=4, y=5, z=6)
        actual = u + v
        assert actual.x == 5
        assert actual.y == 7
        assert actual.z == 9
        actual = actual - v
        assert actual.x == 1
        assert actual.y == 2
        assert actual.z == 3

    def test_length_squared_example(self):
        u = Vector3(x=1, y=2, z=3)
        assert u.length_squared() == 14

    def test_length_example(self):
        u = Vector3(x=1, y=1, z=1)
        assert u.length() == math.sqrt(3)

    def test_dot_perpendicular_vector_is_zero(self):
        u = Vector3(x=1, y=0, z=0)
        v = Vector3(x=0, y=1, z=0)
        assert u.dot(v) == 0

    def test_dot_of_unit_vector_is_one(self):
        u = Vector3(x=0, y=1, z=0)
        v = Vector3(x=0, y=1, z=0)
        assert u.dot(v) == 1

    def test_cross_of_vector_is_perpendicular(self):
        u = Vector3(x=0.5, y=0.5, z=0)
        v = Vector3(x=-0.5, y=0.5, z=0)
        actual = u.cross(v)
        assert actual.x == 0
        assert actual.y == 0
        assert actual.z != 0

    def test_cross_uv_and_vu_point_in_opposite_direction(self):
        u = Vector3(x=1, y=2, z=3)
        v = Vector3(x=2, y=3, z=1)
        c0 = u.cross(v)
        c1 = v.cross(u)
        assert c0.x == -c1.x
        assert c0.y == -c1.y
        assert c0.z == -c1.z

    def test_normalized_vector_has_length_one(self):
        u = Vector3(x=1, y=1, z=0)
        n = u.normalized()
        assert n.length() == pytest.approx(1.0)

    def test_equality_compares_values(self):
        assert Vector3(x=1, y=2, z=3) == Vector3(x=1, y=2, z=3)
        assert Vector3(x=1, y=2, z=3) != Vector3(x=0, y=0, z=0)

    def test_hash_is_based_on_values(self):
        u = Vector3(x=1, y=2, z=3)
        v = Vector3(x=1, y=2, z=3)
        assert hash(u) == hash(v)
