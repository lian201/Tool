# Tool
Python写的工具类


### tinypng
使用tinypng压缩png图片

> 先安装tinify **pip install --upgrade tinify**

> 每个key每月可压缩500张图片，key在 https://tinypng.com/developers 申请

1.将需要压缩的图片放在uncompressed文件夹下

2.执行tinypng.py

3.压缩后的图片会在compressed文件夹下

### qiniu
上传图片到七牛云存储

> 在七牛申请ak，sk

> 获取自己的外链前缀和空间名

1.把需要上传的图片放在up_file文件夹里

2.执行qiniu_update.py

