# -*- coding: utf-8 -*-
import glob

import cv2

import click

DOT_PATH = './images/dot_image/'
MOVIE_PATH = './output/'


def make_mp4(file_header):
    img_array = []
    for file_name in sorted(glob.glob(DOT_PATH + file_header + '*.png')):
        print('load: {}'.format(file_name))
        img = cv2.imread(file_name)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    name = MOVIE_PATH + file_header + '.mp4'
    out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MP4V'), 5.0, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


@click.command()
@click.option('--file_header', '-f', type=str, default='')
def main(file_header):
    make_mp4(file_header)


if __name__ == '__main__':
    main()
