
class ViewPlane:

    def __init__(self, hres, vres, pixel_size, gamma):
        self._hres = hres
        self._vres = vres
        self._pixel_size = pixel_size
        self._gamma = gamma
        self._inv_gamma = 1.0 / gamma

    @property
    def horizontal_resolution(self):
        return self._hres

    @property
    def vertical_resolution(self):
        return self._vres

    @property
    def pixel_size(self):
        return self._pixel_size

    @property
    def gamma(self):
        return self.gamma

    @property
    def inv_gamma(self):
        return self.inv_gamma
