#!/usr/bin/env python

import numpy

from .. import filter


x = numpy.array(
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ],
    dtype=numpy.float32,
)


def test_low_pass_filter():
    y = filter._low_pass_filter(x.shape, 1)
    assert numpy.all(x == y)
    z = filter._high_pass_filter(x.shape, 1)
    assert numpy.all(z == 1.0 - y)


def test_lowpass():
    y = filter._lowpass(3, x)
    assert numpy.allclose(x, y)


if __name__ == '__main__':
    pass
