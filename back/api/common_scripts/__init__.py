"""общие скрипты для данного сайта."""
import cv2
import pathlib
import os
# import numpy as np

# from .. import app


def create_file(file, path, preview=False, prefix="",
                number=0, preview_width=200, subfolder=False,
                subfolder_name=""):
    """создает файл по заданному пути."""
    if number > 0:
        if subfolder:
            path = os.path.join(path, subfolder_name + '_' + str(number))
            if not os.path.exists(path):
                os.mkdir(path)
            filename = prefix + ".png"
            preview_name = prefix + "_preview.png"
        else:
            filename = prefix + '_' + str(number) + ".png"
            preview_name = prefix + '_' + str(number) + "_preview.png"
        filepath = os.path.join(path, filename)
        file.save(filepath)
        if preview:
            img = cv2.imread(filepath)
            width = img.shape[0]
            scale = preview_width / width
            new_width = round(width * scale)
            new_height = round(img.shape[1] * scale)
            # print(cv2.resize)
            file_img = cv2.resize(img, (new_height, new_width))
            filepath = os.path.join(path, preview_name)
            cv2.imwrite(filepath, file_img)
        return filepath
    # print(dir(path['FOLDER_MATERIAL']))
