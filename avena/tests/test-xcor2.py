#!/usr/bin/env python

from numpy import all, array

from .. import np, xcor2


def test_xcor2_shape():
    x = (3, 3)
    y = (1, 1)
    z = (4, 4)
    assert xcor2._xcor2_shape((x, y)) == z


def test_center():
    x = array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
    y = array([[2, 3], [3, 4], [4, 5]])
    assert all(xcor2._center(x, y.shape) == y)


def test_xcor2():
    x = array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    y = array([[1]])
    z = xcor2._xcor2(x, y)
    assert np.peak(z) == (1, 1)


if __name__ == '__main__':
    pass
