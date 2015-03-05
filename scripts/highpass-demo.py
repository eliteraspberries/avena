#!/usr/bin/env python2

'''Apply a high-pass filter to an image.

Usage:
    highpass-demo.py <image> <pixels>
    highpass-demo.py -h | --help

Options:
    -h, --help      Print this help.
'''

from docopt import docopt

from avena import image, filter


if __name__ == '__main__':

    arguments = docopt(__doc__)
    filename = arguments['<image>']
    pixels = float(arguments['<pixels>'])

    img = image.read(filename, normalize=True)
    highpass_img = filter.highpass(img, pixels, pixels)

    print image.save(highpass_img, filename, random=True, normalize=True)
