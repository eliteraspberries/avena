#!/usr/bin/env python

"""Map functions onto image arrays."""


import numpy

from . import image, np


def map_to_channels(func, img):
    """Map a function onto the channels of an image array."""
    channels = image.get_channels(img)
    first = next(channels)
    z = func(first)
    for channel in channels:
        z = numpy.dstack((z, func(channel)))
    return z


def _num_tiles(shape, tile_shape):
    m, n = shape
    a, b = tile_shape
    p = int(numpy.ceil(float(m) / a))
    q = int(numpy.ceil(float(n) / b))
    return (p, q)


def _tile_view(tile_shape, array, coords):
    a, b = tile_shape
    i, j = coords
    return array[(i * a):(i * a + a), (j * b):(j * b + b)]


def _map_to_tiles(tile_shape, func, array):
    a, b = tile_shape
    m, n = _num_tiles(array.shape, tile_shape)
    array = np._zeropad(array, (m * a, n * b))
    result = func(array[:a, :b])
    c, d = result.shape
    result = np._zeropad(result, (m * c, n * d))
    indices = ((i, j) for i in range(m) for j in range(n))
    for (i, j) in indices:
        x = _tile_view((a, b), array, (i, j))
        z = _tile_view((c, d), result, (i, j))
        z[:, :] = func(x)
    return result


if __name__ == '__main__':
    pass
