#!/usr/bin/env python

import numpy

from .. import map


def test_map_to_channels():
    def f(x):
        return x + 1
    x = numpy.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    y = numpy.dstack((x, x, x))
    z = map.map_to_channels(f, y)
    assert numpy.all(z == y + 1)


def test_num_tiles():
    assert map._num_tiles((1, 1), (1, 1)) == (1, 1)
    assert map._num_tiles((1, 2), (1, 1)) == (1, 2)


def test_tile_view():
    x = numpy.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    y = numpy.array([[1, 2, 3]])
    z = map._tile_view((1, 3), x, (0, 0))
    assert numpy.all(z == y)
    y = numpy.array([[2, 3, 4]])
    z = map._tile_view((1, 3), x, (1, 0))
    assert numpy.all(z == y)


def test_map_to_tiles():
    x = numpy.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    def f(a):
        return a + 1
    for shape in [(1, 1), (1, 3)]:
        y = numpy.array([[2, 3, 4], [3, 4, 5], [4, 5, 6]])
        z = map._map_to_tiles(shape, f, x)
        assert numpy.all(z == y)


if __name__ == '__main__':
    pass
