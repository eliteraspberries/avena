#!/usr/bin/env python

import numpy

from .. import np


x = numpy.array([8, 16, 32], dtype='uint8')

y = numpy.array([8. / 256., 16. / 256., 32. / 256.], dtype='float32')


def test_from_uint8():
    assert numpy.all(np.from_uint8(x) == y)


def test_to_uint8():
    assert numpy.all(np.to_uint8(y) == x)


def test_clip():

    x = numpy.random.random_sample(100)
    assert all(x >= 0.) and all(x <= 1.)

    x -= 0.1
    np.clip(x, (0., 1.))
    assert numpy.all(x >= 0.)

    x *= 1.1
    np.clip(x, (0., 1.))
    assert numpy.all(x <= 1.)


def test_peak():
    x = numpy.array([[1, 2, 3], [2, 10, 4], [4, 5, 6]])
    assert np.peak(x) == (1, 1)


def test_zeropad():
    x = numpy.array([[1]])
    y = numpy.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    z = np._zeropad(x, y.shape)
    assert numpy.all(z == y)


if __name__ == '__main__':
    pass
