#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7/17:04
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : site_analyze.py
# @Software: PyCharm

import pandas as pd
from pylab import *


mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def Site(df):
    Beijing_site = ['北京-东城区', '北京-丰台区', '北京-大兴区', '北京-延庆区', '北京-房山区',
                    '北京-昌平区', '北京-朝阳区', '北京-海淀区', '北京-石景山区', '北京-西城区',
                    '北京-通州区', '北京-门头沟区','北京-顺义区']
    site = df.groupby('company_site').count()
    for i in site.index:
        if i in Beijing_site:
            pass
        else:
            site = site.drop(i)
    ax = plt.gca()
    for i in ax.spines:
        ax.spines[i].set_color('none')
    ax.yaxis.grid(True)
    plt.bar(site['title'].index,site['title'].values,color = 'royalblue')
    plt.xticks(size='small', rotation=30)
    for x,y in zip(site['title'].index,site['title'].values):
        plt.text(x, y, '%.0f' % y, ha='center', va='bottom')
    plt.title('前程无忧Python招聘地区分布')
    plt.show()
    return plt

if __name__ == '__main__':
    df = pd.read_csv('51job.csv', encoding='gbk')
    Site(df)