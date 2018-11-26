# -*- coding: utf-8 -*-
"""
   File Name：     散点图
   Product:        PyCharm
   Project:    python4
   File:       散点图.py
   Author :       ZXR
   date：          2018/11/22
   time:           17:06
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import itertools

#画散点图用plt.scatter(x,y),画连续曲线用plt.plot(x,y)
#plt.xticks(loc,label)可以自定义x轴刻度的显示，第一个参数表示的是第二个参数label显示的位置loc
#plt.autoscale(tight = True) 可以自动调整图像显示的最佳化比例
'''
x = np.random.randint(0,28,1000)
y = np.random.randint(600,8000,1000)
plt.scatter(x,y)
plt.title('网站流量')
plt.xlabel('时间')
plt.ylabel('点击量/小时')
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()
'''
'''
fig = plt.figure()
plt.axis([0, 100, 0, 1])
plt.ion()
for i in range(100):
    y = np.random.random()
    plt.autoscale()
    plt.scatter(i, y)
    plt.pause(0.01)
#plt.ioff()
#plt.show()
'''
chushi = 6
a = np.zeros((chushi,chushi,chushi))
for i in range(0,chushi):
    b1 = np.random.randint(2,size = (chushi,chushi))
    a[i] = b1
    #print(a)

from mpl_toolkits.mplot3d import Axes3D
#3D表面形状的绘制
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')

u = np.linspace(0,2*np.pi,100)
v = np.linspace(0,np.pi,100)
x = 10*np.outer(np.cos(u),np.sin(v))
y = 10*np.outer(np.sin(u),np.sin(v))
z = 10*np.outer(np.ones(np.size(u)),np.cos(v))

ax.plot_surface(x,y,z,color='b')
plt.show()

#3D直线(曲线)的绘制
import matplotlib as mpl

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection = '3d')
theta = np.linspace(-4*np.pi,4*np.pi,100)
z = np.linspace(-2,2,100)
r = z**2 +1
x = r*np.sin(theta)
y = r*np.cos(theta)
ax.plot(x,y,z,label='parametric curve')
ax.legend()
plt.show()
