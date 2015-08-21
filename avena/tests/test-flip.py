#!/usr/bin/env python

from numpy import all, array

from avena import flip


def test_flip_vertical():
    x = array([[1], [2], [3]])
    assert all(flip._flip_vertical(flip._flip_vertical(x)) == x)
    y = array([[3], [2], [1]])
    assert all(flip._flip_vertical(x) == y)


def test_flip_horizontal():
    x = array([[1, 2, 3]])
    assert all(flip._flip_horizontal(flip._flip_horizontal(x)) == x)
    y = array([[3, 2, 1]])
    assert all(flip._flip_horizontal(x) == y)


if __name__ == '__main__':
    pass
