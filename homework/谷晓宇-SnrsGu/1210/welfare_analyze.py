#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9/18:53
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : welfare_analyze.py
# @Software: PyCharm

from wordcloud import WordCloud
import pandas as pd

def Wekfare(text):
    wordcloud = WordCloud(background_color="white",width=1000, height=1000, margin=2,font_path='./fonts/simhei.ttf').generate(text)
    image = wordcloud.to_image()
    image.show()
    return image

if __name__ == '__main__':
    df = pd.read_csv('51job.csv', encoding='gbk')
    text = str(list(df.company_welfare.values))
    Wekfare(text)