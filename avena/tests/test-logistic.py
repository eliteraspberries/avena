#!/usr/bin/env python

from numpy import all, random

from .. import logistic


def test_logistic():
    x = random.random_sample(100)
    x *= 10.0
    x -= 5.0
    for k in [1.0, 2.0, 5.0, 10.0]:
        y = logistic._logistic(k, x)
        assert all(y >= 0.0) and all(y <= 1.0)


if __name__ == '__main__':
    pass
