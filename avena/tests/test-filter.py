#!/usr/bin/env python

from numpy import all, allclose, array, float32

from .. import filter


x = array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
], dtype=float32)


def test_low_pass_filter():
    y = filter._low_pass_filter(x.shape, 1)
    assert all(x == y)
    z = filter._high_pass_filter(x.shape, 1)
    assert all(z == 1.0 - y)


def test_lowpass():
    y = filter._lowpass(3, x)
    assert allclose(x, y)


if __name__ == '__main__':
    pass
