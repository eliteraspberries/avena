#!/usr/bin/env python2

'''Apply a high-pass filter to an image.

Usage:
    highpass-demo.py <image> <radius>
    highpass-demo.py -h | --help

Options:
    -h, --help      Print this help.
'''

from docopt import docopt

from avena import image, filter


if __name__ == '__main__':

    arguments = docopt(__doc__)
    filename = arguments['<image>']
    radius = float(arguments['<radius>'])

    img = image.read(filename, normalize=True)
    highpass_img = filter.highpass(img, radius)

    print image.save(highpass_img, filename, random=True, normalize=True)
