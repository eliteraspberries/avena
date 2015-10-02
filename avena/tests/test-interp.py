#!/usr/bin/env python

from numpy import all, allclose, array, float32, max

from .. import interp


def test_interp2():
    x = array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ], dtype=float32)
    y = interp._interp2(1.0, x)
    assert allclose(x, y)


if __name__ == '__main__':
    pass
