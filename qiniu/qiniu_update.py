# -*- coding: utf-8 -*-

import os
import Config
from qiniu import Auth, put_file, etag

# ak sk
access_key = Config.qiniu_ak
secret_key = Config.qiniu_sk

# 构建鉴权对象
q = Auth(access_key, secret_key)

# 外链前缀
base_url = Config.qiniu_base_url

# 要上传的空间名
bucket_name = Config.qiniu_bucket_name

# 根目录
rootDir = os.path.dirname(__file__) + "/up_file/"

for root, dirs, files in os.walk(rootDir):
    size = files.__len__()
    count = 1
    for name in files:
        if (name.startswith(".")):
            size -= 1
            continue
        sourceFile = rootDir + name
        print("正在上传%s  %d/%d" % (name, count, size))
        token = q.upload_token(bucket_name, name, 3600)
        ret, info = put_file(token, name, sourceFile)
        if (info.status_code == 200):
            assert ret['key'] == name
            assert ret['hash'] == etag(sourceFile)
            print("上传完成，外链url为--  %s" % (base_url + name))
