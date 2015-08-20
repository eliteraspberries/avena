#!/usr/bin/env python

'''2D array tiling'''


from numpy import zeros as _zeros

from . import flip, image


def _tile9_periodic_shape(shape):
    m, n = shape
    return (3 * m, 3 * n)


def _tile9_periodic(x):
    m, n = x.shape
    z = _zeros(_tile9_periodic_shape((m, n)), dtype=x.dtype)
    xfv = flip.flip_vertical(x)
    xfh = flip.flip_horizontal(x)
    xfb = flip.flip_horizontal(flip.flip_vertical(x))
    tile0 = z[m:(2 * m), n:(2 * n)]
    tile1 = z[:m, n:(2 * n)]
    tile2 = z[:m, (2 * n):(3 * n)]
    tile3 = z[m:(2 * m), (2 * n):(3 * n)]
    tile4 = z[(2 * m):(3 * m), (2 * n):(3 * n)]
    tile5 = z[(2 * m):(3 * m), n:(2 * n)]
    tile6 = z[(2 * m):(3 * m), :n]
    tile7 = z[m:(2 * m), :n]
    tile8 = z[:m, :n]
    tile0[:, :] = x[:, :]
    tile1[:, :] = xfv[:, :]
    tile2[:, :] = xfb[:, :]
    tile3[:, :] = xfh[:, :]
    tile4[:, :] = xfb[:, :]
    tile5[:, :] = xfv[:, :]
    tile6[:, :] = xfb[:, :]
    tile7[:, :] = xfh[:, :]
    tile8[:, :] = xfb[:, :]
    return z


def tile9_periodic(img):
    '''Tile an image into a 3x3 periodic grid.'''
    return image.map_to_channels(
        _tile9_periodic,
        _tile9_periodic_shape,
        img,
    )


if __name__ == '__main__':
    pass
