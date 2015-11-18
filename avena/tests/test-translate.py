#!/usr/bin/env python

import numpy

from .. import translate


def test_translate():
    x = numpy.array([[1, 2, 3], [2, 3, 4], [4, 5, 6]])
    assert numpy.all(translate._translate((0, 0), x) == x)


if __name__ == '__main__':
    pass
