# -*- coding:utf-8 -*-
from os.path import splitext
import glob
from PIL import Image


def get_all_file(filename):
    files = glob.glob(filename)
    return files


def to_ather_file(files, type):
    for jpg in files:
        im = Image.open(jpg)
        png = splitext(jpg)[0] + "." + type
        im.save(png)
        print("png")


if __name__ == "__main__":
    filename = "./image/*.[Jj][Pp][Gg]"
    files = get_all_file(filename)
    to_ather_file(files, "png")

# http://silencewt.github.io/2015/02/01/python-%E6%89%B9%E9%87%8F%E6%9B%B4%E6%8D%A2%E5%9B%BE%E7%89%87%E6%A0%BC%E5%BC%8F%E8%84%9A%E6%9C%AC/
# 原地址↑
