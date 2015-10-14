#!/usr/bin/env python

from numpy import all, array

from .. import translate


def test_translate():
    x = array([[1, 2, 3], [2, 3, 4], [4, 5, 6]])
    assert all(translate._translate((0, 0), x) == x)


if __name__ == '__main__':
    pass
