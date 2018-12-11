#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9/19:18
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : skill_analyze.py
# @Software: PyCharm

from wordcloud import WordCloud
import pandas as pd


def Skill(text):
    text = text.replace('xa0', '').replace('任职要求', '').replace('岗位要求', '').replace('岗位职责','').replace('职位要求', '') \
        .replace('职位描述', '').replace('任职资格', '').replace('工作职责', '').replace('职能类别', '').replace('加分项', '').replace('\\t', '').replace('\\n', '')
    wordcloud = WordCloud(background_color="white", width=1000, height=1000, margin=2,
                          font_path='./fonts/simhei.ttf').generate(text)
    image = wordcloud.to_image()
    image.show()
    return image

if __name__ == '__main__':
    df = pd.read_csv('51job.csv', encoding='gbk')
    text = str(list(df.job_info.values))
    Skill(text)