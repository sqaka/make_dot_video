# -*- coding: utf-8 -*-
import glob
import os

import cv2


DOT_PATH = './images/dot_image/'
MOVIE_PATH = './output/'


def make_mp4(file_header, k_param):
    img_array = []
    for file_name in sorted(glob.glob(DOT_PATH + file_header + '*.png')):
        print('load: {}'.format(file_name))
        img = cv2.imread(file_name)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    os.makedirs(MOVIE_PATH, exist_ok=True)
    name = '{}{}_k{}.mp4'.format(MOVIE_PATH, file_header, k_param)
    out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MP4V'), 5.0, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


def main(file_header, k_param):
    make_mp4(file_header, k_param)


if __name__ == '__main__':
    main()
