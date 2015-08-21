#!/usr/bin/env python

from numpy import all, array

from .. import tile


def test_tile9_periodic():
    x = array([[1]])
    y = array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert all(tile._tile9_periodic(x) == y)


if __name__ == '__main__':
    pass
