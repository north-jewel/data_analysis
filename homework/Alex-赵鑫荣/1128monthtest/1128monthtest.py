# -*- coding: utf-8 -*-
"""
   File Name：     1128monthtest
   Product:        PyCharm
   Project:    python4
   File:       1128monthtest.py
   Author :       ZXR
   date：          2018/11/28
   time:           14:19
"""
import matplotlib.pyplot as plt

def hist_plt(
        data,labels,
        title='1802C班违纪情况',xlabel='违纪情况',ylabel='违纪次数',
        width=0.8,
        left=[2,4,6,8,10],
        ylim = [0,45],):
    '''
    输入数据和x轴标签
    :param data: 数据信息
    :param labels: x轴上将要显示的信息
    :param title: 图的挑剔
    :param xlabel: x轴的总标签
    :param ylabel: y轴的总标签
    :param width:柱状图的宽度
    :param left: 柱状图的位置分布
    :param ylim: y轴的显示刻度限制
    :return:画出对应数据，对应信息的柱状图
    '''
    plt.rcParams['font.sans-serif']='SimHei'
    fig,ax = plt.subplots()
    ax.set(ylim = ylim,title=title,xlabel=xlabel,ylabel=ylabel)
    plt.bar(left, data, width,tick_label=labels)
    plt.grid(axis="y")
    for x,y in zip(*[left,data]):
        plt.annotate(labels[left.index(x)]+':'+str(y), xy=(x,y),
                     xytext=(x,y),xycoords='data',
                     textcoords='offset points',
                     arrowprops=dict(arrowstyle = '->',
                                     connectionstyle = 'arc3,rad =1.8'))
hist_plt(data = [39, 8, 0, 3, 6],
         labels = ['未带电脑总数', '未带手机总数', '未关投影仪次数', '未关门窗次数', '校查违纪'])