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
import random
import numpy as np
import pandas as pd

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
    ax.set_axisbelow(True)
    plt.grid(axis="y")
    for x,y in zip(*[left,data]):
        plt.annotate(labels[left.index(x)]+':'+str(y), xy=(x,y),
                     xytext=(x,y),xycoords='data',
                     textcoords='offset points',
                     arrowprops=dict(arrowstyle = '->',
                                     connectionstyle = 'arc3,rad =1.8'))
# hist_plt(data = [39, 8, 0, 3, 6],
#          labels = ['未带电脑总数', '未带手机总数', '未关投影仪次数', '未关门窗次数', '校查违纪'])

def hists_plt2(
        x_labels,#plt_label,
        title='9.25~10.25月度违纪对比',xlabel='班级',ylabel='违纪情况',
        fontsize=15,width=0.8,
        left=[2,4,6,8,10,12,14,16,18,20],
        ylim = [0,45],**kwargs):
    '''
    通过传入的数据画出叠加的柱状图
    :param x_labels: x轴上显示的labels
    :param plt_label: 图例示例labels
    :param title: 图的标题
    :param xlabel: x轴的总label
    :param ylabel: y轴的总label
    :param width: 柱状图的宽度
    :param left:  每个柱子的x轴坐标
    :param ylim:  y轴的刻度限制
    :param kwargs: 传入的数据
    :return: 画出图例
    '''
    plt.rcParams['font.sans-serif']='SimHei'
    fig,ax = plt.subplots()
    ax.set_ylim(ylim)
    ax.set_title(title,fontsize=fontsize)
    ax.set_xlabel(xlabel=xlabel,fontsize=fontsize)
    ax.set_ylabel(ylabel=ylabel,fontsize=fontsize)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    kwargs_list = list(kwargs)
    #bottom_list = []
    for i in range(len(kwargs)):
        if i == 0:
            plt.bar(left,kwargs[kwargs_list[0]],width,label=kwargs_list[0])
            print(type(plt.bar(left,kwargs[kwargs_list[0]],width,label=kwargs_list[0])))
        else:
            bottom_list = [kwargs[kwargs_list[x]] for x in range(0,i)]
            bottom = [sum(t) for t in zip(*bottom_list)]
            #bottom = list(np.array(bottom_list).cumsum(axis=0)[-1])
            plt.bar(left,kwargs[kwargs_list[i]],width,bottom = bottom,label=kwargs_list[i])
            #bottom_list = []
    plt.xticks(left,x_labels,size=15)
    plt.yticks(size=15)
    ax.set_axisbelow(True)
    plt.grid(b = True,axis="y")
    plt.legend(loc=8, bbox_to_anchor=(0.5, -0.15),ncol=15,fontsize=15)
    data_list = [sum(e) for e in zip(*list(kwargs.values()))]
    for x, y in zip(*[left, data_list]):
        ana_text = '\n'
        for k,v in kwargs.items():
            ana_text += k + ':'+str(v[left.index(x)])+'\n'
        # print(ana_text)
        plt.text(x,y+0.8,ana_text,fontsize = 13,color='blue',ha='center',
                 bbox = dict(boxstyle="round", fc='w', ec="0.5", lw=1,alpha = 0.8))

# hists_plt2(x_labels = ['1802C', '1803C', '1804C', '1805C', '1806C1','1806C2','1807C1','1807C2','1808C1','1808C2'],
#            # plt_label = ['未带电脑总数','未带手机总数','未关投影仪次数','未关门窗次数','校查违纪'],
#            未带电脑总数 = [6,7,8,9,1,2,3,4,5,6],
#            未带手机总数 = [random.randint(0,10)for i in range(10)],
#            未关投影仪次数 = [random.randint(0,10)for i in range(10)],
#            未关门窗次数 = [random.randint(0,10)for i in range(10)],
#            校查违纪 = [random.randint(0,10)for i in range(10)],
#            )


#plt.plot(kind='bar',stacked=True)   堆叠画出柱状图


def hists_bar2(
        x_labels,#plt_label,
        title='9.25~10.25月度违纪对比',xlabel='班级',ylabel='违纪情况',
        fontsize = 15,width=0.8,
        left=[2,4,6,8,10,12,14,16,18,20],
        ylim = [0,45],**kwargs):
    '''
    通过传入的数据画出叠加的柱状图
    :param x_labels: x轴上显示的labels
    :param plt_label: 图例示例labels
    :param title: 图的标题
    :param xlabel: x轴的总label
    :param ylabel: y轴的总label
    :param width: 柱状图的宽度
    :param left:  每个柱子的x轴坐标
    :param ylim:  y轴的刻度限制
    :param kwargs: 传入的数据
    :return: 画出图例
    '''
    plt.rcParams['font.sans-serif']='SimHei'
    fig,ax = plt.subplots()
    ax.set_ylim(ylim)
    ax.set_title(title, fontsize=fontsize)
    ax.set_xlabel(xlabel=xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel=ylabel, fontsize=fontsize)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    kwargs_list = list(kwargs)
    info_arr = np.array(list(kwargs.values()))
    bottom_arr = info_arr.cumsum(axis=0)
    bottom = None

    for i in range(len(info_arr)):
        if i:
            bottom = bottom_arr[i-1]
        plt.bar(left,info_arr[i],bottom = bottom,width=width,label=kwargs_list[i])

    plt.xticks(left,x_labels,size=20)
    plt.yticks(size=20)
    ax.set_axisbelow(True)
    plt.grid(b = True,axis="y")
    plt.legend(loc=8, bbox_to_anchor=(0.5, -0.15), ncol=15, fontsize=15)
    data_list = [sum(e) for e in zip(*list(kwargs.values()))]
    for x, y in zip(*[left, data_list]):
        ana_text = '\n'
        for k,v in kwargs.items():
            ana_text += k + ':'+str(v[left.index(x)])+'\n'
        # print(ana_text)
        plt.annotate(ana_text, xy=(x, y),
                     xytext=(x, y), xycoords='data',
                     textcoords='offset points',
                     fontsize=14,
                     arrowprops=dict(arrowstyle='->',facecolor= 'r',
                                     connectionstyle='arc3,rad =1.2'))
hists_bar2(x_labels = ['1802C', '1803C', '1804C', '1805C', '1806C1','1806C2','1807C1','1807C2','1808C1','1808C2'],
           # plt_label = ['未带电脑总数','未带手机总数','未关投影仪次数','未关门窗次数','校查违纪'],
           未带电脑总数 = [6,7,8,9,1,2,3,4,5,6],
           未带手机总数 = [random.randint(0,10)for i in range(10)],
           未关投影仪次数 = [random.randint(0,10)for i in range(10)],
           未关门窗次数 = [random.randint(0,10)for i in range(10)],
           校查违纪 = [random.randint(0,10)for i in range(10)],
           )