# -*- coding: utf-8 -*-
import glob
import numpy as np

import cv2

import click

IMAGE_PATH = './images/normal_image/'
DOT_PATH = './images/dot_image/'
ALPHA = 2  # 0.5, 2
K = 16  # 4, 16


def get_image(file_header):
    img_array = []
    for file_name in sorted(glob.glob(IMAGE_PATH + file_header + '*.png')):
        img = cv2.imread(file_name)
        img_array.append(img)
        print(file_name)

    return img_array


def sub_color(src, k):
    Z = src.reshape((-1, 3))
    Z = np.float32(Z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    ret, label, center = cv2.kmeans(
        Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]

    return res.reshape((src.shape))


def mosaic(img, alpha):
    h, w, ch = img.shape

    img = cv2.resize(img, (int(w*alpha), int(h*alpha)))
    img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)

    return img


def pixel_art(img, alpha, k):
    img = mosaic(img, alpha)
    return sub_color(img, k)


def make_dots(img_array, file_header):
    count = 0
    for i in img_array:
        dst = pixel_art(i, ALPHA, K)
        cv2.imwrite(DOT_PATH + file_header +
                    str(count).zfill(4) + '.png', dst)
        print('save: {}{}.png'.format(file_header, str(count).zfill(4)))
        count += 1
    print('=== complete! ===')


@click.command()
@click.option('--file_header', '-f', type=str, default='')
def main(file_header):
    img_array = get_image(file_header)
    make_dots(img_array, file_header)


if __name__ == '__main__':
    main()
