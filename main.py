import glob
import re
import os
import shutil
from pprint import pprint

import fold_id

PYDIR = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.dirname(PYDIR)
INBOX_AFTER = f'{INBOX}/After'

ARCHIVE = os.path.dirname(INBOX)
MOV = '/movie'
IMG = '/img'


def main():

    # ----- AlbumからAfterへ移動
    before = f'{INBOX}/Album/????/??/??/*'
    for i in glob.glob(before):
        shutil.move(i, INBOX_AFTER)

    # ----- Afterの中を走査してゲームフォルダへ
    dir_game = ARCHIVE + '/sw_'
    dir_inbox_glob = f'{INBOX_AFTER}/*'

    for file in glob.glob(dir_inbox_glob):
        for id in fold_id.dict:
            if id in file:
                to = dir_game + fold_id.dict[id]

                # ゲームフォルダがない場合作成
                if os.path.exists(to) is False:
                    FOLD_NAMES = ('', MOV, IMG)
                    [os.mkdir(to + fold_name) for fold_name in FOLD_NAMES]

                to += MOV if '.mp4' in file else IMG
                shutil.move(file, to)


if __name__ == '__main__':
    main()
