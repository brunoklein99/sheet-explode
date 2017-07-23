import random
from os import listdir, path
from os.path import isfile, join
import cv2

path_load = 'K:\\contact-sheets\\sheets'
path_save = 'K:\\contact-sheets\\unlabeled'


def get_thumb(sheet, col, row, col_count, row_count, border_size, margin_left, margin_right, margin_bottom, margin_top):
    sheet_h, sheet_w, _ = sheet.shape
    thumb_h = int((sheet_h - (margin_top + margin_bottom) - ((row_count - 1) * border_size)) / row_count)
    thumb_w = int((sheet_w - (margin_left + margin_right) - ((col_count - 1) * border_size)) / col_count)
    x0 = margin_left
    x0 += ((col - 1) * border_size)
    x0 += ((col - 1) * thumb_w)
    y0 = margin_top
    y0 += ((row - 1) * border_size)
    y0 += ((row - 1) * thumb_h)
    x1 = x0 + thumb_w
    y1 = y0 + thumb_h
    return sheet[y0:y1, x0:x1]


def is_old_sheet(sheet):
    b, g, r = sheet[0, 0]
    return g > b and g > r


if __name__ == "__main__":
    files = [join(path_load, f) for f in listdir(path_load) if isfile(join(path_load, f))]

    for file in files:
        sheet = cv2.imread(file)
        if is_old_sheet(sheet):
            col = random.randint(1, 5)
            row = random.randint(1, 5)
            thumb = get_thumb(sheet, col, row, 5, 5, 8, 5, 8, 8, 80)
        else:
            col = random.randint(1, 4)
            row = random.randint(1, 4)
            thumb = get_thumb(sheet, col, row, 4, 4, 4, 16, 16, 16, 16)
        thumb = cv2.resize(thumb, (256, 256))
        thumb_filename = join(path_save, '{}-{}.'.format(col, row) + path.basename(file))
        cv2.imwrite(thumb_filename, thumb)
