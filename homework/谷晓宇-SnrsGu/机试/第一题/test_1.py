import numpy as np,matplotlib.pyplot as plt
from pylab import *


def Test_1(computer = 0,phone = 0,projector = 0,door = 0,rule = 0,class_n = '1802C'):
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    X = np.arange(5)
    Y = [computer,phone,projector,door,rule]
    plt.xticks([0,1,2,3,4],[r'未带电脑总数',r'未带手机总数',r'未关投影仪总数',r'未关门窗总数',r'校查违纪'])
    plt.title(class_n+'班违纪情况')
    plt.bar(X,Y,width = 0.5)
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.yaxis.grid(True)
    for n,s,a in zip(Y,['未带电脑总数','未带手机总数','未关投影仪总数','未关门窗总数','校查违纪'],X):
        plt.annotate(s,xy = (a,n+1),xycoords = 'data',xytext = (-25,+25),
                     textcoords = 'offset pixels',arrowprops = dict(connectionstyle = 'arc3,rad = 0.5'))
    for x, y in zip(X,Y):
        plt.text(x,y,'%.0f'%y,ha='center', va='bottom')
    plt.show()
    return plt

Test_1(3,7,10,5,20)