#!/usr/bin/env python

from numpy import all, allclose, array, dstack
from os import remove
from os.path import sep, split

from .. import image, utils


def test_get_channels():
    x = array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    y = dstack((x, x, x))
    for z in image.get_channels(y):
        assert all(z == x)


def test_read_save():
    f = split(__file__)[0] + sep + 'drink.png'
    x = image.read(f)
    tmp = utils.rand_filename(f)
    try:
        image.save(x, tmp)
        y = image.read(tmp)
        assert allclose(x, y, rtol=1e-4, atol=1e-1)
    finally:
        remove(tmp)


if __name__ == '__main__':
    pass
