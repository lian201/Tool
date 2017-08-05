#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import tinify
import Config

tinify.key = Config.pinypng_key

rootDir = os.path.dirname(__file__)
sourceDir = "/Users/zhe/Documents/_tinypng_file/uncompressed/"
saveDir = "/Users/zhe/Documents/_tinypng_file/compressed/"

for root, dirs, files in os.walk(sourceDir):
    size = files.__len__()
    count = 1
    for name in files:
        if (name.startswith(".")):
            size -= 1
            continue
        print("正在处理 %d/%d  %s " % (count, size, name))
        source = tinify.from_file(sourceDir + name)
        source.to_file(saveDir + name)
        count += 1
    print("处理完成")
