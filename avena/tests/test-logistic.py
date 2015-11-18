#!/usr/bin/env python

import numpy

from .. import logistic


def test_logistic():
    x = numpy.random.random_sample(100)
    x -= 0.5
    x *= 10.0
    for k in [1.0, 2.0, 5.0, 10.0]:
        y = logistic._logistic(k, (0.0, 1.0), 0.5, x)
        assert numpy.all(y >= 0.0) and all(y <= 1.0)


if __name__ == '__main__':
    pass
