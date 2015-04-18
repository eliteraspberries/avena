#!/usr/bin/env python2

'''2D spatial filtering with the FFT'''


from functools import partial
from numpy import (
    array as _array,
    empty as _empty,
    multiply as _multiply,
    real as _real,
    vectorize as _vectorize,
)
from numpy.fft import (
    fftshift as _fftshift,
    ifftshift as _ifftshift,
    irfft2 as _irfft2,
    rfft2 as _rfft2,
)

from . import image, utils


def __in_circle(a, b, r, coords):
    x, y = coords
    d = (x - a) ** 2 + (y - b) ** 2
    if d < r ** 2:
        return 1.0
    else:
        return 0.0


def _indices_array(array):
    m, n = array.shape[:2]
    indices = _array(
        [[(i, j) for j in range(n)] for i in range(m)],
        dtype=('f4,f4'),
    )
    return indices


def _high_pass_filter(array, radius):
    m, n = array.shape[:2]
    indices = _indices_array(array)
    _in_circle = partial(__in_circle, m // 2, n // 2, radius)
    _v_in_circle = _vectorize(_in_circle)
    return 1.0 - _v_in_circle(indices)


def highpass(array, radius):
    '''Apply a 2D high-pass filter to an image array.'''
    z = _empty(array.shape, dtype=array.dtype)
    for i, c in enumerate(image.get_channels(array)):
        C = _rfft2(c)
        C = _fftshift(C)
        filter = _high_pass_filter(C, radius)
        _multiply(C, filter, out=C)
        C = _ifftshift(C)
        c = _irfft2(C, s=c.shape)
        c = _real(c)
        if utils.depth(array) > 1:
            z[:, :, i] = c
        else:
            z = c
    return z


if __name__ == '__main__':
    pass
