#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9/20:28
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : salary_analyze.py
# @Software: PyCharm

import pandas as pd
# import re
# import numpy as np
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def Salary(df):

    salary = str(list(df.salary.values))
    w_rex = '([\d+\.\d]*)-([\d+\.\d]*)万/月'
    k_rex = '([\d+\.\d]*)-([\d+\.\d]*)千/月'
    print(type(salary))
    w_x = re.findall(w_rex,salary)  #获得待处理的万元每月的数据
    k_x = re.findall(k_rex,salary)  #获得待处理的千元每月的数据
    w_xx = eval(str(w_x).replace('(','').replace(')',''))
    k_xx = eval(str(k_x).replace('(','').replace(')',''))
    w = []
    k = []
    for w_ in w_xx:
        w.append(int(eval(w_)*10))
    for k_ in k_xx:
        w.append(eval(k_))
    zong = w+k
    range_x = [i for i in range(0,max(zong)+1)]
    num = np.bincount(zong)
    xxx = list(zip(range_x,num))
    for i in xxx[:]:
        if i[1] <= 300:
            xxx.remove(i)
    a = []
    b = []
    for i in xxx:
        a.append(i[0])
        b.append(i[1])
    plt.plot(a,b,color = 'blue')
    ax = plt.gca()
    for i in ax.spines:
        ax.spines[i].set_color('none')
    ax.grid()
    plt.title('前程无忧Python招聘工资分布')
    # plt.xticks([10, 15, 20, 25, 30, 35, 40], [r'$10k/m$', r'$15k/m$', r'$20k/m$', r'$25k/m$', r'$30k/m$', r'$35k/m$', r'$40k/m$'])
    plt.xlabel('薪资区间（千/月）')
    plt.show()

    return plt

if __name__ == '__main__':
    df = pd.read_csv('51job.csv', encoding='gbk')
    Salary(df)