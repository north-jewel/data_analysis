#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9/19:51
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : edu_analyze.py
# @Software: PyCharm

import pandas as pd
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def Edu(df):
    edu_scope = ['初中及以下','本科','博士','中专','大专','硕士']
    edu = df.groupby('edu_required').count()
    for i in edu.index:
        if i in edu_scope:
            pass
        else:
            edu = edu.drop(i)
    plt.barh(edu['title'].index,edu['title'].values,color = 'dodgerblue')
    ax = plt.gca()
    for i in ax.spines:
        ax.spines[i].set_color('none')
    ax.xaxis.grid(True)
    plt.title('前程无忧Python招聘学历要求')
    plt.show()
    return plt

if __name__ == '__main__':
    df = pd.read_csv('51job.csv', encoding='gbk')
    Edu(df)