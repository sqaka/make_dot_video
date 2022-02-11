# -*- coding: utf-8 -*-
import os
import sys

import cv2

import click

VIDEO_PATH = './video/'
IMAGE_PATH = './images/normal_image/'


def movie_to_image(file_header):
    cap = cv2.VideoCapture(VIDEO_PATH + file_header + '.mp4')

    if not cap.isOpened():
        print('Data loading error!')
        sys.exit()

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    print('width:{}, height:{}, count:{}, fps:{}'.format(
        width, height, count, fps))

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    count = 0
    os.makedirs(IMAGE_PATH, exist_ok=True)
    while True:
        is_image, frame_img = cap.read()
        if is_image:
            cv2.imwrite(IMAGE_PATH + file_header +
                        str(count).zfill(digit) + '.png', frame_img)
            print('save: ' + file_header + str(count).zfill(digit) + '.png')
        else:
            break
        count += 1

    cap.release()
    print('=== complete! ===')


@click.command()
@click.option('--file_header', '-f', type=str, default='')
def main(file_header):
    movie_to_image(file_header)


if __name__ == '__main__':
    main()
