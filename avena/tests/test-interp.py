#!/usr/bin/env python

import numpy

from .. import interp


def test_interp2():
    x = numpy.array(
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ],
        dtype=numpy.float32,
    )
    y = interp._interp2(1.0, x)
    assert numpy.allclose(x, y)


if __name__ == '__main__':
    pass
