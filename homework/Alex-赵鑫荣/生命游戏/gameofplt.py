# -*- coding: utf-8 -*-
"""
   File Name：     gameoflife
   Product:        PyCharm
   Project:    python4
   File:       gameoflife.py
   Author :       ZXR
   date：          2018/11/12
   time:           14:22
"""
import numpy as np
import matplotlib.pyplot as plt

# print(np.random.randint(0,2,(10,10)))
class gamelife:

    def __init__(self,x_dot,y_dot,dot_px=10):
        self.x_dot = x_dot
        self.y_dot = y_dot
        self.dot_px = dot_px
        self.source_a = np.random.randint(0,2,(self.x_dot,self.y_dot))
        self.copy_a = np.copy(self.source_a)


    def has_counts(self,x, y):
        """
        传入一个具体的坐标，判断周围有几个“生命”
        0表示空白，1表示生命
        :param x:       x-1,y-1  x-1,y  x-1,y+1
                        x,y-1    x,y    x,y+1
                        x+1,y-1  x+1,y  x+1,y+1
        :param y:
        :return: 周围存活细胞的个数
        """
        count_num = 0
        for i in (x-1,x,x+1):
            for j in (y-1, y, y+1):
                if i == x and j == y:
                    continue
                if i < 0 or j < 0 or i >= self.x_dot or j >= self.y_dot:
                    continue
                if self.source_a[i][j] == 1:
                    count_num += 1
        #print('第一个方法', count_num)
        return count_num


    def live_or_die(self,life_counts,x,y):
        '''
        此函数为判断函数，通过周围存活细胞个数判断此细胞是否存活
        :param life_counts: 某个坐标周围存活的细胞个数
        :return: 返回该细胞是否存活
        '''
        if life_counts == 3:
            return 1
        if life_counts > 3 or life_counts < 2:
            return 0
        if life_counts == 2:
            return self.source_a[x,y]


    def next_array(self,copy_a):
        '''
        输入一个数组，通过调用之前的方法，来生成一个新的数组
        :param source_a:输入一个数组
        :return:生成一个新的数组
        '''
        #copy_a = np.copy(source_a)
        for x in range(self.x_dot):
            for y in range(self.y_dot):
                copy_a[x,y] = self.live_or_die(self.has_counts(x,y),x,y)

        return copy_a


    def main(self,):
        
        fig = plt.figure(figsize = (10,10))
        fig.add_subplot(111)
        plt.rcParams['font.sans-serif'] = 'SimHei'
        from matplotlib import cm    #colormap
        #data = np.random.randint(0,2,(10,10))
        #print(data)
        cmap = cm.Blues    
        plt.title('生命游戏与matplotlib')
        # define a variable to control the main loop
        running = True
        #plt.ion()
        # main loop
        while running:
            
            map = plt.imshow(self.source_a,interpolation = 'nearest',
                             cmap = cmap,aspect = 'auto',vmin = 0,vmax = 1)
            #self.copy_a = np.random.randint(0,1,(self.x_dot,self.y_dot))
            
            for x in range(self.x_dot):
                for y in range(self.y_dot):
                    self.copy_a[x, y] = self.live_or_die(self.has_counts(x, y), x, y)
                    
            plt.pause(0.5)
            self.source_a = np.copy(self.copy_a)
        plt.ioff()
        
if __name__ == '__main__':
    gamelife(60,60).main()
