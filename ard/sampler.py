from ard.vector2 import Vector2
from typing import Any


class Sampler:

    def __init__(self, num_samples: int, num_sets: int) -> None:
        self._num_samples = num_samples
        self._num_sets = num_sets
        self._sets = []  # type: List[List[Vector2]]

    @property
    def num_sets(self) -> int:
        return self._num_sets

    @property
    def num_samples(self) -> int:
        return self._num_samples

    def sample_unit_square(self, set_index: int) -> List[Vector2]:
        return self._sets[set_index]


class StandardSampler(Sampler):

    def __init__(self):
        Sampler.__init__(self, num_samples=1, num_sets=1)
        self._sets.append([Vector2(x=0.5, y=0.5)])


class JitteredSampler(Sampler):

    def __init__(self, samples_per_axis: int, num_sets: int, random: Any) -> None:
        Sampler.__init__(self,
                         num_samples=samples_per_axis*samples_per_axis,
                         num_sets=num_sets)

        self._samples_per_axis = samples_per_axis

        for s in range(self.num_sets):
            samples = []
            for j in range(self._samples_per_axis):
                for k in range(self._samples_per_axis):
                    x = (k + random.random()) / self._samples_per_axis
                    y = (j + random.random()) / self._samples_per_axis
                    samples.append(Vector2(x=x, y=y))
            self._sets.append(samples)
