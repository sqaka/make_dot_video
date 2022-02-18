import glob
import os
import re
import shutil

from utils.eraser import erase_dot
from utils.eraser import erase_image
from utils.pick_flame import movie_to_image
from utils.make_dots import main as make_dots
from utils.connect_pict import make_mp4

PALAM = [3, 4, 8]
VIDEO_PATH = './video/'
MOVE_PATH = './video/done/'


def name_cleaner(file_header):
    file_header = re.sub(f'{VIDEO_PATH}', '', file_header)
    file_header = re.sub('.mp4', '', file_header)
    return file_header


def move_video(file_header):
    os.makedirs(MOVE_PATH, exist_ok=True)
    shutil.move('{}{}.mp4'.format(VIDEO_PATH, file_header),
                '{}{}.mp4'.format(MOVE_PATH, file_header))


def main():
    for file_header in sorted(glob.glob(VIDEO_PATH + '*.mp4')):
        file_header = name_cleaner(file_header)
        movie_to_image(file_header)
        for i in PALAM:
            make_dots(file_header, int(i))
            make_mp4(file_header, str(i))
            erase_dot(file_header)
        erase_image(file_header)
        move_video(file_header)


if __name__ == '__main__':
    main()
