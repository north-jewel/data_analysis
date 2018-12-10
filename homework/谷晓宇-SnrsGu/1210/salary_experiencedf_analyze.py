#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10/8:32
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : salary_experiencedf_analyze.py
# @Software: PyCharm


from functools import reduce
import pandas as pd
# import re
# import numpy as np
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def alter(list):
    a = str(list)
    w_rex = '([\d+\.\d]*)-([\d+\.\d]*)万/月'
    k_rex = '([\d+\.\d]*)-([\d+\.\d]*)千/月'
    w_x = re.findall(w_rex, a)  # 获得待处理的万元每月的数据
    k_x = re.findall(k_rex, a)  # 获得待处理的千元每月的数据
    w_xx = eval(str(w_x).replace('(', '').replace(')', ''))
    k_xx = eval(str(k_x).replace('(', '').replace(')', ''))
    w = []
    k = []
    for w_ in w_xx:
        w.append(int(eval(w_) * 10))
    for k_ in k_xx:
        w.append(eval(k_))
    zong = w + k
    return reduce(lambda x, y: x + y, zong) / len(zong)

def salary_experiencedf(df):
    exp = ['10年以上经验', '1年经验', '2年经验', '3-4年经验', '5-7年经验', '8-9年经验', '无工作经验']
    salary_mean = []
    for i in exp:
        a = int(alter(list(df[df['experience_required'].isin([i])].dropna(how='any').salary.values)))
        salary_mean.append(a)
    plt.bar(exp,salary_mean,color = 'red')
    ax = plt.gca()
    for i in ax.spines:
        ax.spines[i].set_color('none')
    ax.yaxis.grid(True)
    for x,y in zip(exp,salary_mean):
        plt.text(x, y, '%.0f-k/m' % y, ha='center', va='bottom')
    plt.title('前程无忧Python招聘经验与薪资关系')
    plt.ylabel('薪资区间（千/月）')
    plt.show()
    return plt


if __name__ == '__main__':
    df = pd.read_csv('51job.csv', encoding='gbk')
    salary_experiencedf(df)