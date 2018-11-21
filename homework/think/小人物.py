import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from pylab import mpl
import matplotlib
import matplotlib.pyplot as plt
#plt.rcParams['font.sas-serig']=['SimHei'] #用来正常显示中文标签
#plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#mpl.rcParams['font.sans-serif'] = ['SimHei']
'''
x=np.linspace(-5,5,30,endpoint=True)
y=x**2
plt.title(u'平方图')
plt.plot(x,y,'y.',label=u'平方图')
plt.legend()
plt.show()
'''
theta = np.arange(0, 2 * np.pi,  np.pi / 100)

theta = np.append(theta, [2 * np.pi])
#print(theta)
x = np.cos(theta*2)
y = np.sin(theta*2)
ban=np.arange(0,np.pi,np.pi/100)
ban_x=np.cos(ban)
ban_y=np.sin(ban)
e=np.linspace(-1,1,200)
b=e**2
v = np.linspace(0, 10, 100)
v.shape = (100, 1)
plt.plot(x-1.5, y+1,'ko')
plt.plot(x+1.5, y+1,'ko')
plt.plot(x/6+1.5, y/6+1,'ko')
plt.plot(x/6-1.5, y/6+1,'ko')
plt.plot(x/3*v,y/3-0.2*v+4,'p')
plt.plot(x/3,y/3-0.2,'p')
plt.plot(e,b-2,'o')
plt.plot(ban_x/2,ban_y/2+1,'ko')
plt.plot(ban_y+2.9,ban_x,'p')
plt.plot(-ban_y-2.9,ban_x,'ro')
plt.plot(-ban_y/3-3,ban_x/2,'k')
plt.plot(ban_y/3+3,ban_x/2,'k')
z_x=np.linspace(-4,0,5)
plt.plot(ban_x/3+2.9,ban_x/3/6+1.2,'ko')
plt.plot(ban/3-3.5,ban_x*0+1,'ko')
print(z_x)
plt.plot(z_x/12-3,z_x*0)
plt.plot(z_x/12+3.3,z_x*0)
new_x=np.linspace(-3,-2,100)
plt.plot(new_x,np.abs(new_x),'go')
plt.plot(x * 3, y * 3, 'r',alpha=0.5)
plt.plot(3,5,'g')
plt.show()
print(matplotlib.matplotlib_fname())