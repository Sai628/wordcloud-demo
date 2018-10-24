# coding=utf-8

import codecs
import time
import random

from bs4 import BeautifulSoup
import jieba
import requests
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        return ''


def get_comment(html):
    soup = BeautifulSoup(html, 'html.parser')
    comments_list = []
    comment_nodes = soup.select('.comment > p')
    for node in comment_nodes:
        comments_list.append(node.get_text().strip().replace("\n", "") + u'\n')
    return comments_list


def save_comment_text(file_path):
    pre_url = "https://movie.douban.com/subject/24773958/comments?"
    depth = 8
    with open(file_path, 'a', encoding='utf-8') as f:
        for i in range(depth):
            url = pre_url + 'start=' + str(20 * i) + '&limit=20&sort=new_score&' + 'status=P'
            print("get comments from: %s" % url)
            html = get_html(url)
            f.writelines(get_comment(html))
            f.flush()
            time.sleep(1 + float(random.randint(1, 20)) / 20)


def cut_words(file_path):
    text = ''
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n')
            text += ' '.join(jieba.cut(line))
            text += ' '
    with codecs.open('data/text.txt', 'a', encoding='utf-8') as f:
        f.write(text)


def draw_wordcloud():
    with codecs.open('data/text.txt', encoding='utf-8') as f:
        comment_text = f.read()

    # 设置背景图片
    color_mask = np.array(Image.open("mask.jpg"))
    # 停用词设置
    Stopwords = [u'就是', u'电影', u'你们', u'这么', u'不过', u'但是',
                 u'除了', u'时候', u'已经', u'可以', u'只是', u'还是',
                 u'只有', u'不要', u'觉得', u'，'u'。']
    # 设置词云属性
    wc = WordCloud(font_path="simhei.ttf",
                   background_color='white',
                   max_words=500,
                   max_font_size=150,
                   min_font_size=4,
                   mask=color_mask,
                   stopwords=Stopwords)
    # 生成词云, 可以用 generate 输入全部文本, 也可以我们计算好词频后使用 generate_from_frequencies 函数
    wc.generate(comment_text)
    # 保存图片
    wc.to_file("data/comment_cloud.jpg")
    # 从背景图片生成颜色值(注意图片的大小)
    image_colors = ImageColorGenerator(color_mask)

    # 显示图片
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")

    # 绘制词云
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis("off")

    plt.figure()
    plt.imshow(color_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    file_path = "data/comment.txt"
    save_comment_text(file_path)
    cut_words(file_path)
    draw_wordcloud()
