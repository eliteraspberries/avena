#!/usr/bin/env python

import numpy

from .. import tile


def test_tile9_periodic():
    x = numpy.array([[1]])
    y = numpy.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert numpy.all(tile._tile9_periodic(x) == y)


if __name__ == '__main__':
    pass
