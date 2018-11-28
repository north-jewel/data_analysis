import numpy as np
import matplotlib.pyplot as plt
from gameoflife import gamelife

class gameofplt(gamelife):    #继承gameoflife中的gamelife类

    #def __init__(self):
        #super(gameofplt, self).__init__()
        #self.source_a = np.random.randint(0, 2, (self.x_dot, self.y_dot))
        #self.copy_a = np.copy(self.source_a)

    def mainplt(self):
        '''
        用plt.imshow()方法画出gameoflife
        :return:
        # data = np.random.randint(0,2,(10,10))
        # print(data)
        map = plt.imshow(data,interpolation = 'nearest',
                cmap = cmap,aspect = 'auto',vmin = 0,vmax = 1)
        #interpolation 差值 vmin最小值 白色
        '''
        fig = plt.figure(figsize=(8, 8))    #创建画布，且使画布大小为10*10
        fig.add_subplot(111)         #在此画布上添加子图
        plt.rcParams['font.sans-serif'] = 'SimHei'      #设置黑体字
        from matplotlib import cm  # colormap            #导入colormap
        cmap = cm.Oranges        #橘色系
        plt.title('生命游戏与matplotlib')    #设置子图标题
        running = True
        # plt.ion()     #打开交互模式
        while running:
            #用plt.imshow()方法画出DataFrame，interpolation 差值(最近的) vmin最小值 白色
            map = plt.imshow(self.source_a, interpolation='nearest',
                                cmap=cmap, aspect='auto', vmin=0, vmax=1)
            # self.copy_a = np.random.randint(0,1,(self.x_dot,self.y_dot))
            self.copy_a = self.next_array(self.copy_a)    #调用next_array()方法来计算下一个数组
            plt.pause(0.5)     #间歇时间0.5s
            self.source_a = np.copy(self.copy_a)
            plt.clf()    #清空画布
        plt.ioff()     #关闭交互模式


    def mainscatter(self):
        '''
        用散点图来画gameoflife
        :return:
        '''
        fig2 = plt.figure(figsize=(8, 8))    #创建画布
        fig2.add_subplot(111)
        plt.rcParams['font.sans-serif'] = 'SimHei'
        plt.title('生命游戏与matplotlib散点图')
        x_list = []    #散点图的x轴坐标点列表
        y_list = []    #散点图的y轴坐标点列表
        running = True
        plt.ion()      #打开交互模式
        while running:
            self.copy_a = self.next_array(self.copy_a)    #调用next_array()方法计算下一个数组
            for x in range(self.x_dot):
                for y in range(self.y_dot):
                    if self.source_a[x, y]:  #如果满足细胞存活条件：
                        x_list.append(x)    #将x添加到x轴列表里
                        y_list.append(y)    #将y添加到y轴列表里
            plt.scatter(x_list, y_list)     #画出所有存活细胞的散点图
            plt.pause(0.5)  # 间歇时间0.5s
            x_list = []
            y_list = []
            self.source_a = np.copy(self.copy_a)
            plt.clf()    #清空画布
            #fig2.add_subplot(111)
        plt.ioff()     #关闭交互模式

    def mainfill(self):
        '''
        用fill_between来画图
        :return:
        '''
        fig3 = plt.figure(figsize=(8, 8))  # 创建画布
        fig3.add_subplot(111)
        plt.rcParams['font.sans-serif'] = 'SimHei'
        plt.title('生命游戏与matplotlib散点图')
        running = True
        plt.ion()  # 打开交互模式
        print('创建时的figure',fig3.number)
        while running:
            print(fig3.number)
            self.copy_a = self.next_array(self.copy_a)  # 调用next_array()方法计算下一个数组
            #print(self.source_a)
            for x in range(self.x_dot):
                for y in range(self.y_dot):
                    if self.source_a[x, y]:  # 如果满足细胞存活条件：
                        plt.fill_between([x,x+1],y,y+1,color = 'red')
            plt.pause(0.5)  # 间歇时间0.5s
            print('循环时的figure',fig3.number)
            self.source_a = np.copy(self.copy_a)
            plt.clf()  # 清空画布

if __name__ == '__main__':
    gameofplt(80, 80).mainscatter()