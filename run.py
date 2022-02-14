import os
import shutil

import click

from utils.eraser import erase_dot
from utils.eraser import erase_image
from utils.pick_flame import main as pick_flame
from utils.make_dots import main as make_dots
from utils.connect_pict import main as connect_pict

PALAM = [4, 16]
VIDEO_PATH = './video/'
MOVE_PATH = './video/done/'


def move_video(file_header):
    os.makedirs(MOVE_PATH, exist_ok=True)
    shutil.move('{}{}.mp4'.format(VIDEO_PATH, file_header),
                '{}{}.mp4'.format(MOVE_PATH, file_header))


@click.command()
@click.option('--file_header', '-f', type=str, default='')
def main(file_header):
    pick_flame(file_header)
    for i in PALAM:
        make_dots(file_header, int(i))
        connect_pict(file_header, str(i))
        erase_dot(file_header)
    erase_image(file_header)
    move_video(file_header)


if __name__ == '__main__':
    main()
