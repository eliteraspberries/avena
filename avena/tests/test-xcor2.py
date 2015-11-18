#!/usr/bin/env python

import numpy

from .. import np, xcor2


def test_xcor2_shape():
    x = (3, 3)
    y = (1, 1)
    z = (4, 4)
    assert xcor2._xcor2_shape((x, y)) == z


def test_center():
    x = numpy.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
    y = numpy.array([[2, 3], [3, 4], [4, 5]])
    assert numpy.all(xcor2._center(x, y.shape) == y)


def test_xcor2():
    x = numpy.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    y = numpy.array([[1]])
    z = xcor2._xcor2(x, y)
    assert np.peak(z) == (1, 1)


if __name__ == '__main__':
    pass
