#!/usr/bin/env python

'''Vertical or horizontal flipping of 2D images'''


from . import image


def _flip_vertical(array):
    return array[::-1, :]


def flip_vertical(img):
    '''Flip an image array vertically.'''
    return image.map_to_channels(
        _flip_vertical,
        lambda (x, y): (x, y),
        img,
    )


def _flip_horizontal(array):
    return array[:, ::-1]


def flip_horizontal(img):
    '''Flip an image array horizontally.'''
    return image.map_to_channels(
        _flip_horizontal,
        lambda (x, y): (x, y),
        img,
    )


if __name__ == '__main__':
    pass
