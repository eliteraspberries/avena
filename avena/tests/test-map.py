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


if __name__ == '__main__':
    pass
