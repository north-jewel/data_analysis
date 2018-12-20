#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/10/9:24
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : salary_site_analyze.py
# @Software: PyCharm

from functools import reduce
import pandas as pd
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


def salary_site(df):
    area = ['北京-东城区', '北京-丰台区', '北京-大兴区', '北京-延庆区', '北京-房山区',
                    '北京-昌平区', '北京-朝阳区', '北京-海淀区', '北京-石景山区', '北京-西城区',
                    '北京-通州区', '北京-门头沟区','北京-顺义区']
    salary_mean = []
    for i in area:
        a = int(alter(list(df[df['company_site'].isin([i])].dropna(how='any').salary.values)))
        salary_mean.append(a)
    print(salary_mean)
    plt.barh(area, salary_mean, color='lime')
    ax = plt.gca()
    for i in ax.spines:
        ax.spines[i].set_color('none')
    ax.xaxis.grid(True)
    plt.title('前程无忧Python招聘地区与工资关系')
    plt.xlabel('薪资区间（千/月）')
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('51job.csv', encoding='gbk')
    salary_site(df)