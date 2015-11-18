#!/usr/bin/env python

import numpy

from .. import flip


def test_flip_vertical():
    x = numpy.array([[1], [2], [3]])
    assert numpy.all(flip._flip_vertical(flip._flip_vertical(x)) == x)
    y = numpy.array([[3], [2], [1]])
    assert numpy.all(flip._flip_vertical(x) == y)


def test_flip_horizontal():
    x = numpy.array([[1, 2, 3]])
    assert numpy.all(flip._flip_horizontal(flip._flip_horizontal(x)) == x)
    y = numpy.array([[3, 2, 1]])
    assert numpy.all(flip._flip_horizontal(x) == y)


if __name__ == '__main__':
    pass
