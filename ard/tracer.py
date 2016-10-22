
class Tracer:

    def __init__(self):
        return

    def trace_ray(self, ray, world):
        shade_rec = self.hit_objects(ray, world.scene_objects)

        if shade_rec is None:
            return world.background_color
        else:
            return shade_rec.color

    def hit_objects(self, ray, objects):
        min_result = None

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
