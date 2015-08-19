#!/usr/bin/env python

'''Vertical or horizontal flipping of 2D images'''


def flip_vertical(array):
    '''Flip an array vertically.'''
    return array[::-1, :]


def flip_horizontal(array):
    '''Flip an array horizontally.'''
    return array[:, ::-1]


if __name__ == '__main__':
    pass
