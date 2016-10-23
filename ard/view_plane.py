from ard.sampler import Sampler


class ViewPlane:

    def __init__(self, hres: int, vres: int, pixel_size: float,
                 gamma: float, sampler: Sampler) -> None:
        self._hres = hres
        self._vres = vres
        self._pixel_size = pixel_size
        self._gamma = gamma
        self._inv_gamma = 1.0 / gamma
        self._sampler = sampler

    @property
    def horizontal_resolution(self) -> int:
        return self._hres

    @property
    def vertical_resolution(self) -> int:
        return self._vres

    @property
    def pixel_size(self) -> float:
        return self._pixel_size

    @property
    def gamma(self) -> float:
        return self._gamma

    @property
    def inv_gamma(self) -> float:
        return self._inv_gamma

    @property
    def sampler(self) -> Sampler:
        return self._sampler
