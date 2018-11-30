import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

a=np.random.randint(0,100)
B={'未带电脑总数':np.random.randint(0,100),
   '未带手机总数':np.random.randint(0,100),
   '未关投影次数': np.random.randint(0, 100),
   '未关门窗次数': np.random.randint(0, 100),
   '校查违纪': np.random.randint(0, 100)}

t='1802c违纪情况'


def method(dict,title):
    key=np.array(list(dict.keys()))
    value=np.array(list(dict.values()))
    len_dict=len(dict)
    x=np.array(range(len_dict))
    #fig, axl = plt.subplots(3, 3)
    plt.title(title)
    print(value)
    #for i in  range(len_dict-1):
    plt.bar(x,value)
    plt.xticks(x,key)
    for i, y in zip(x, value):
        plt.text(i, y+1, str(key[i])+str(value[i]), ha='center', va='bottom')
    plt.show()
#method(B,t)
class_dict={'1802':{'未带电脑总数':np.random.randint(0,100),
                    '未带手机总数':np.random.randint(0,100),
                    '未关投影次数': np.random.randint(0, 100),
                    '未关门窗次数': np.random.randint(0, 100),
                    '校查违纪': np.random.randint(0, 100)},
            '1803':{'未带电脑总数':np.random.randint(0,100),
                    '未带手机总数':np.random.randint(0,100),
                    '未关投影次数': np.random.randint(0, 100),
                    '未关门窗次数': np.random.randint(0, 100),
                    '校查违纪': np.random.randint(0, 100)},
            '1804': {'未带电脑总数': np.random.randint(0, 100),
                     '未带手机总数': np.random.randint(0, 100),
                     '未关投影次数': np.random.randint(0, 100),
                     '未关门窗次数': np.random.randint(0, 100),
                     '校查违纪': np.random.randint(0, 100)},
            '1805': {'未带电脑总数': np.random.randint(0, 100),
                     '未带手机总数': np.random.randint(0, 100),
                     '未关投影次数': np.random.randint(0, 100),
                     '未关门窗次数': np.random.randint(0, 100),
                     '校查违纪': np.random.randint(0, 100)},
            '1806': {'未带电脑总数': np.random.randint(0, 100),
                     '未带手机总数': np.random.randint(0, 100),
                     '未关投影次数': np.random.randint(0, 100),
                     '未关门窗次数': np.random.randint(0, 100),
                     '校查违纪': np.random.randint(0, 100)},
}
def maxzip(*items):
    return [sum(values) for values in zip(*items)]
def methods(dict,title):
    key = np.array(list(dict.keys()))
    len_dict = len(dict)
    new_dict={}
    value=np.array(list(dict[key[0]].keys()))
    for i in  range(len_dict):
        new_dict[key[i]]=list(dict[key[i]].values())
    print(new_dict)
    new_key = np.array(list(new_dict.keys()))
    new_value = np.array(list(new_dict.values()))
    # print(new_value[0])
    x = np.array(range(len_dict))
    plt.title(title)
    plt.xticks(x,key)
    plt.grid(axis='y')
    plt.bar(x,np.array(new_value[0]),width=0.35,align='center',color='r',alpha=0.8,label=value[0])
    plt.bar(x, np.array(new_value[1]), width=0.35, align='center', color='y',bottom=np.array(new_value[0]), alpha=0.8,label=value[1])
    #print(sum(np.array(new_value[0]),np.array(new_value[1])))
    plt.bar(x, np.array(new_value[2]), width=0.35, align='center', color='b', bottom=maxzip(np.array(new_value[0]),np.array(new_value[1])), alpha=0.8,label=value[2])
    plt.bar(x, np.array(new_value[3]), width=0.35, align='center', color='g', bottom=maxzip(np.array(new_value[0]),np.array(new_value[1]),np.array(new_value[2])), alpha=0.8,label=value[3])
    plt.bar(x, np.array(new_value[4]), width=0.35, align='center', color='pink', bottom=maxzip(np.array(new_value[0]),np.array(new_value[1]),np.array(new_value[2]),np.array(new_value[3])),  alpha=0.8,label=value[4])
    #plt.legend(bbox_to_anchor=(0,-0.2,1.3,-1),loc=3,ncol=5,mode='expand',borderaxespad=0.1)
    #plt.legend()
    plt.legend(loc=2, bbox_to_anchor=(-0.05,-0.07),borderaxespad = 0.,ncol=5) 
    plt.show()
methods(class_dict,t)






