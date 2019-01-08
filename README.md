# Tool
Python写的工具类



### tinypng
使用tinypng压缩png图片

> 每个key每月可压缩500张图片，key在 https://tinypng.com/developers 申请

```
先安装tinify和click 

pip3 install --upgrade tinify

pip3 install click
```
在同目录下创建Config.py文件，在文件中写入key

    eg: pinypng_key = "xxxx"


- 默认配置 python3 tinypng.py

    1.将需要压缩的图片放在uncompressed文件夹下
    
    2.执行tinypng.py
    
    3.压缩后的图片会在compressed文件夹下
   
- 处理单张图片 python3 tinypng.py -f 图片路径/xx.jpg

    处理后文件名前添加_
    
    eg: python3 tinypng.py -f /Users/zhe/Pictures/a.png  生成_a.png

- 处理文件夹中的图片  python3 tinypng.py -d 文件夹路径 

    在文件夹下生成_tinypng文件夹放处理后的文件
    
    eg: python3 tinypng.py -d /Users/zhe/Pictures  在Pictures下生成_tinypng文件夹存放处理好的图片
    


### qiniu
上传文件到七牛云存储，图片上传至imgs空间，文件上传至files空间

```
安装qiniu
pip install qiniu
```

在同目录下创建Config.py文件，在文件中写入所需配置项

```
qiniu_ak = "xxxx"
qiniu_sk = "xxxx"
qiniu_base_url_img = "xxxx"
qiniu_base_url_file = "xxxx"
qiniu_bucket_name_img = "imgs"
qiniu_bucket_name_file = "files"   
```

> 在七牛申请ak，sk

> 获取自己的外链前缀和空间名

- 默认配置 python3 qiniu_upload.py

    1.把需要上传的图片放在up_file文件夹里

    2.执行qiniu_update.py

- 上传单文件

    python3 qiniu_update.py -f /Users/zhe/Pictures/a.png
    
- 上传文件夹里所有文件

    python3 qiniu_update.py -d /Users/zhe/Pictures


### smms
> https://sm.ms/ 一个免费图床

> API地址  https://sm.ms/doc/

- 上传单文件

    python3 smms_upload.py -f /Users/zhe/Pictures/a.png
    
- 上传文件夹里所有文件

    python3 smms_upload.py -d /Users/zhe/Pictures/

