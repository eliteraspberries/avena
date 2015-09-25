#!/usr/bin/env python

from numpy import all, array, dstack

from .. import image


def test_get_channels():
    x = array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    y = dstack((x, x, x))
    for z in image.get_channels(y):
        assert all(z == x)


def test_map_to_channels():
    def f(x):
        return x + 1
    x = array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    y = dstack((x, x, x))
    z = image.map_to_channels(
        f,
        lambda shape: shape,
        y,
    )
    assert all(z == y + 1)


if __name__ == '__main__':
    pass
