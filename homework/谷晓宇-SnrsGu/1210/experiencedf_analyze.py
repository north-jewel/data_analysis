#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7/16:36
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : experiencedf_analyze.py
# @Software: PyCharm

import pandas as pd
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def Experiencedf(df):
    experiencedf = df.groupby('experience_required').count()
    ax = plt.gca()
    for i in ax.spines:
        ax.spines[i].set_color('none')
    ax.yaxis.grid(True)
    plt.bar(experiencedf['title'].index,experiencedf['title'].values,color = 'chartreuse')
    # plt.xticks(experiencedf['title'].index, experiencedf['title'].index, size='small', rotation=30)
    plt.ylim(0,2500)
    for x,y in zip(experiencedf['title'].index,experiencedf['title'].values):
        plt.text(x, y, '%.0f' % y, ha='center', va='bottom')
    plt.title('前程无忧Python招聘经验分布')
    plt.show()
    return plt

if __name__ == '__main__':
    df = pd.read_csv('51job.csv', encoding='gbk')
    Experiencedf(df)