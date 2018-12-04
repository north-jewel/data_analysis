import matplotlib.pyplot as plt


#散点图,marker形状
plt.scatter(x,y,s = 大小,c = 颜色,marker = '*')

#柱形图,
plt.bar(x,height = y,bottom = '从哪里开始图色')



#饼状图，参数：数据，要不要突出，数据标签，
#百分比的小数位，带不带阴影，从多少度开始画
plt.pie(sizes,explode = explode,
        labels = labels,autopct = '%1.2f%%',shadow = True,startangle = 90)

plt.plot(x,y,color = 'red',linewidth = 4.0,linestyle = '--',label='sin',alpha = 0.5)
#linewidth 线宽， linestyle：线的样式，label:图例，alpha:透明度
plt.legend() #调用这个函数后label才会生效



plt.figure(1)#要画几个图

#正常显示中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']   #中文
mpl.rcParams['axes.unicode_minus']=False     #负号


plt.title('表头名字')
plt.xlabel('x轴名字')
plt.ylabel('y轴名字')

#设置这个图的大小，第三个参数是宽，第四个是高。单位是倍数。
#facecolor:背景颜色
plt.axes([1,0,1,1],facecolor = 'red')

#把画的图保存到本地
plt.savefig(r'C:/Users/赵孟/Desktop/微信.png')

#三个参数，把画布分成3行3列，这个图占第一个位置
ax = fig.add_subplot(331)

#调用以下函数后会把画出的图变成网格图
plt.grid()

#指定轴的数值范围
plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1.5])


#操作轴之前必须调用这个函数
ax = plt.gca()

#使右边的轴消失
ax.spines['right'].set_color('none')

#让左轴和下轴移到1的位置
ax.spines['left'].set_position(('data',1))
ax.spines['bottom'].set_position(('data',1))

#修改x和y轴标记位置
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')

#设置x和y轴的比例
ax.set_aspect(1)


#改x轴上标记
plt.yticks(原标记,np.linspace(-1,1,5))
plt.xticks([-np.pi,-np.pi/2,0.9,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$\pi$'])


#填充颜色
plt.fill(x,y,'颜色')

#迭代x,y轴的标签，改变其样式
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)#字体大小
    label.set_bbox(dict(facecolor='yellow',edgecolor='red',alpha = 0.8))
    #facecolor:标签背景颜色，edgecolor:边框颜色，alpha透明度


#注释，
plt.annotate("(4,4)",xy=(4,4),xycoords='data',xytext=(3,2),
            arrowprops = dict(arrowstyle='<|-|>'))
# xytext 默认标记的坐标的绝对位置,没有的话用xy参数的
# textcoords 指定相对位置,相对点 和相对像素
# 箭头arrowprops  箭头风格connectionstyle
    
