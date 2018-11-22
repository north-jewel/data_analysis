import numpy as np
import matplotlib.pyplot as plt
from gameoflife import gamelife

class gameofplt(gamelife):    #继承gameoflife类

    def __init__(self,x_dot,y_dot,):
        super(gameofplt, self).__init__(x_dot,y_dot)
        self.source_a = np.random.randint(0, 2, (self.x_dot, self.y_dot))
        self.copy_a = np.copy(self.source_a)

    def mainplt(self):
            fig = plt.figure(figsize=(10, 10))    #创建画布，且使画布大小为10*10
            fig.add_subplot(111)         #在此画布上添加子图
            plt.rcParams['font.sans-serif'] = 'SimHei'      #设置黑体字
            from matplotlib import cm  # colormap            #导入colormap
            # data = np.random.randint(0,2,(10,10))
            # print(data)
            cmap = cm.Oranges        #蓝色系
            plt.title('生命游戏与matplotlib')    #设置子图标题
            # define a variable to control the main loop
            running = True
            # main loop
            while running:
                #用plt.imshow()方法画出DataFrame，interpolation 差值(最近的) vmin最小值 白色
                map = plt.imshow(self.source_a, interpolation='nearest',
                                 cmap=cmap, aspect='auto', vmin=0, vmax=1)
                # self.copy_a = np.random.randint(0,1,(self.x_dot,self.y_dot))
                self.copy_a = self.next_array(self.copy_a)
                '''
                for x in range(self.x_dot):
                    for y in range(self.y_dot):
                        self.copy_a[x, y] = self.live_or_die(self.has_counts(x, y), x, y)
                '''
                plt.pause(0.5)     #间歇时间0.5s
                self.source_a = np.copy(self.copy_a)
            plt.ioff()     #关闭交互模式

if __name__ == '__main__':
    gameofplt(60, 60).mainplt()