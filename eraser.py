# -*- coding: utf-8 -*-
import glob
import os

import click

IMAGE_PATH = './images/normal_image/'
DOT_PATH = './images/dot_image/'


def erase_image(file_header):
    for file_name in sorted(glob.glob(IMAGE_PATH + file_header + '*.png')):
        os.remove(file_name)
        print('Delete: {}'.format(file_name))


def erase_dot(file_header):
    for file_name in sorted(glob.glob(DOT_PATH + file_header + '*.png')):
        os.remove(file_name)
        print('Delete: {}'.format(file_name))


@click.command()
@click.option('--file_header', '-f', type=str, default='safety')
def main(file_header):
    erase_image(file_header)
    erase_dot(file_header)


if __name__ == '__main__':
    main()
