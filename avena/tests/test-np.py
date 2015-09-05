#!/usr/bin/env python

from numpy import all, array, random

from .. import np


x = array([8, 16, 32], dtype='uint8')

y = array([8., 16., 32.], dtype='float32')


def test_from_uint8():
    assert all(np.from_uint8(x, 'float32') == y)


def test_to_uint8():
    assert all(np.to_uint8(y / 255.) == x)


def test_clip():

    x = random.random_sample(100)
    assert all(x >= 0.) and all(x <= 1.)

    x -= 0.1
    np.clip(x, (0., 1.))
    assert all(x >= 0.)

    x *= 1.1
    np.clip(x, (0., 1.))
    assert all(x <= 1.)


if __name__ == '__main__':
    pass
