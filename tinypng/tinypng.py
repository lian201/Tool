#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import tinify
import click
import Config

tinify.key = Config.pinypng_key


# 判断是不是图片
def isPic(name):
    # 获取文件名和文件类型
    filename, filetype = os.path.splitext(name)
    if (filetype == ".png" or filetype == ".jpg" or filetype == ".jpeg"):
        return "true"
    else:
        print(name + "不是图片")


# 压缩图片
def compressed(inFile, outFile):
    source = tinify.from_file(inFile)
    source.to_file(outFile)


# 遍历文件夹，压缩图片
def walkFolder(inFolder, outFilder):
    for root, dirs, files in os.walk(inFolder):
        size = files.__len__()
        count = 1
        for name in files:
            if (not isPic(name)):
                size -= 1
                continue
            print("正在处理 %d/%d  %s " % (count, size, name))
            compressed(inFolder + "/" + name, outFilder + "/" + name)
            count += 1
        print("处理完成")
        break


# 没有任何参数，默认对预定文件夹操作
def default():
    sourceDir = "/Users/zhe/Documents/_tinypng_file/uncompressed"
    saveDir = "/Users/zhe/Documents/_tinypng_file/compressed"
    walkFolder(sourceDir, saveDir)


# 压缩单文件
def compressedFile(inFile):
    if (not os.path.isfile(inFile)):
        print("这不是文件")
        return
    # 文件路径
    dirname = os.path.dirname(inFile)
    # 文件名
    basename = os.path.basename(inFile)
    if (not isPic(basename)):
        return
    print("开始处理" + basename)
    compressed(inFile, dirname + "/_" + basename)
    print("处理完成")


# 压缩文件夹下所有文件
def compressedFolder(dir):
    if (not os.path.isdir(dir)):
        print("这不是文件夹")
        return
    saveDir = dir + "/_tinypng"
    if (not os.path.isdir(saveDir)):
        os.mkdir(saveDir)
    walkFolder(dir, saveDir)


@click.command()
@click.option("-f", "--file", default=None, help="对单文件操作")
@click.option("-d", "--dir", default=None, help="对文件夹操作")
def run(file, dir):
    if (file is not None):
        compressedFile(file)
        pass
    elif (dir is not None):
        compressedFolder(dir)
        pass
    else:
        default()
        pass


# 程序入口
if __name__ == "__main__":
    run()
