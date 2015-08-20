#!/usr/bin/env python

'''Read and write image files as NumPy arrays'''


from numpy import (
    asarray as _asarray,
    copy as _copy,
    empty as _empty,
    float32 as _float32,
)
from PIL import Image

from . import np, utils


_DEFAULT_DTYPE = _float32

_PIL_RGB = {
    'R': 0,
    'G': 1,
    'B': 2,
}


def get_channels(img):
    '''Return a list of channels of an image array.'''
    if utils.depth(img) == 1:
        yield img
    else:
        for i in range(utils.depth(img)):
            yield img[:, :, i]


def read(filename, dtype=_DEFAULT_DTYPE, normalize=True):
    '''Read an image file as an array.'''
    img = Image.open(filename)
    arr = _asarray(img, dtype=dtype)
    utils.swap_rgb(arr, _PIL_RGB, to=utils._PREFERRED_RGB)
    if normalize:
        np.normalize(arr)
    return arr


def _pil_save(img, filename):
    pil_img = Image.fromarray(img)
    pil_img.save(filename)
    return


SAVE_NORMALIZED = False


def save(img, filename, random=False, ext=None, normalize=SAVE_NORMALIZED):
    '''Save an image array and return its path.'''
    if random:
        newfile = utils.rand_filename(filename, ext=ext)
    else:
        newfile = filename
    utils.swap_rgb(img, utils._PREFERRED_RGB, to=_PIL_RGB)
    save_img = _copy(img)
    if normalize:
        np.normalize(save_img)
    np.clip(save_img, np._dtype_bounds[str(save_img.dtype)])
    uint8img = np.to_uint8(save_img)
    _pil_save(uint8img, newfile)
    return newfile


if __name__ == '__main__':
    pass
