#!/usr/bin/env python

import numpy
import os

from .. import image, utils


def test_get_channels():
    x = numpy.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    y = numpy.dstack((x, x, x))
    for z in image.get_channels(y):
        assert numpy.all(z == x)


def test_read_save():
    f = os.path.split(__file__)[0] + os.path.sep + 'drink.png'
    x = image.read(f)
    tmp = utils.rand_filename(f)
    try:
        image.save(x, tmp)
        y = image.read(tmp)
        assert numpy.allclose(x, y, rtol=1e-4, atol=1e-1)
    finally:
        os.remove(tmp)


if __name__ == '__main__':
    pass
