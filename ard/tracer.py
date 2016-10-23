from ard.color import Color
from ard.geometric_object import GeometricObject, ShadeRecord, HitResult
from ard.ray import Ray
from ard.world import World
from typing import Optional


class Tracer:

    def __init__(self) -> None:
        return

    def trace_ray(self, ray: Ray, world: World) -> Color:
        shade_rec = self.hit_objects(ray, world.scene_objects)

        if shade_rec is None:
            return world.background_color
        else:
            return shade_rec.color

    def hit_objects(self, ray: Ray, objects: List[GeometricObject]) -> Optional[ShadeRecord]:
        min_result = None  # type: Optional[HitResult]

        for object in objects:
            result = object.hit(ray)
            if result is None:
                continue
            if min_result is None or result.tmin < min_result.tmin:
                min_result = result

        if min_result is None:
            return None
        else:
            return min_result.shade_record
