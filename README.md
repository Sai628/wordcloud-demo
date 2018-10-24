# Word Cloud 库使用示例程序

## 概述:

使用 Python 的 requests 库, 爬取豆瓣上对于 "复仇者联盟3" 这部电影的影评数据, 然后利用 jieba 库进行分词后, 使用词云库 word-cloud 生成词云图片.

## 运行环境: 

> Python 3.6.5+

## 运行步骤:

1. 创建 virtualenv 环境
```bash
$ virtualenv venv
$ source venv/bin/activate
```

2. 安装依赖库
```bash
$ pip install -r requirements.txt
```

3. 运行
```bash
$ python main.py
```

## 运行效果:

![](http://oo8lgm5bz.bkt.clouddn.com/2018-10-24-word-cloud-demo-comment_cloud.jpg?imageView2/2/w/480)