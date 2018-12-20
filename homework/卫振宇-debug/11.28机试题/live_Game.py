# !usr/bin/env python
# -*- coding:utf-8 -*-
# author: 卫振宇
# time: 2018/11/14
import numpy as np
import pygame
#import matplotlib.pyplot as plt
#from matplotlib import cm
class LiveGame:

    def __init__(self,X_DOT,Y_DOT,DOT_PX = 10):
        self.X_DOT = X_DOT
        self.Y_DOT = Y_DOT
        self.DOT_PX = DOT_PX
        self.source_a = np.random.randint(0,2,(self.X_DOT,self.Y_DOT))
        self.copy_a = np.copy(self.source_a)

    def has_counts(self,x,y):
        counts = 0
        for i in (x - 1, x, x + 1):
            for j in (y - 1, y, y + 1):
                if i == x and j == y:
                    continue
                if i < 0 or j < 0 or i >= self.X_DOT or j >= self.Y_DOT:
                    continue
                if self.source_a[i][j] == 1:
                    counts += 1
        # print('第一个方法', count_num)
        return counts
    def next_array(self,copy_a):
        '''
        输入一个数组，通过调用之前的方法，来生成一个新的数组
        :param source_a:输入一个数组
        :return:生成一个新的数组
        '''
        #copy_a = np.copy(source_a)
        for x in range(self.X_DOT):
            for y in range(self.Y_DOT):
                copy_a[x,y] = self.live_or_die(self.has_counts(x,y),x,y)

        return copy_a
    def live_or_die(self,live_counts,x,y):
        if live_counts == 3:
            return 1
        if live_counts>3 or live_counts<2:
            return 0
        if live_counts == 2:
            return self.source_a[x,y]

    def main(self):
        # 初始化pygame模块
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("minimal program")

        screen = pygame.display.set_mode((self.DOT_PX * self.X_DOT, self.DOT_PX * self.Y_DOT))

        running = True
        while running:
            screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('......')
                    running = False
            self.copy_a = self.next_array(self.copy_a)
            for x in range(self.X_DOT):
                for y in range(self.Y_DOT):


                    if self.source_a[x,y] == 1:
                        screen.fill((0, 0, 255), (y * self.DOT_PX, x * self.DOT_PX, self.DOT_PX, self.DOT_PX))
                        pygame.draw.rect(screen, (0, 255, 0), (y * self.DOT_PX, x * self.DOT_PX, self.DOT_PX, self.DOT_PX), 2)

            pygame.display.update()
            self.source_a = np.copy(self.copy_a)
            pygame.time.wait(500)
    def matplot(self):
        fig = plt.figure(figsize = (8,8))
        fig,ax = plt.subplots()
        plt.rcParams['font.sans-serif'] = 'SimHei'

        plt.title('生命游戏与matplotlib')  # 设置子图标题
        cmap = cm.Oranges
        running = True
        # plt.ion()     #打开交互模式
        while running:
            # 用plt.imshow()方法画出DataFrame，interpolation 差值(最近的) vmin最小值 白色
            map = plt.imshow(self.source_a, interpolation='nearest',
                             cmap=cmap, aspect='auto', vmin=0, vmax=1)
            # self.copy_a = np.random.randint(0,1,(self.x_dot,self.y_dot))
            self.copy_a = self.next_array(self.copy_a)  # 调用next_array()方法来计算下一个数组
            plt.pause(0.5)  # 间歇时间0.5s
            self.source_a = self.copy_a
            plt.clf()  # 清空画布
        plt.ioff()  # 关闭交互模式

    def sandian(self):
        fig2 = plt.figure(figsize=(8, 8))  # 创建画布
        fig2.add_subplot(111)
        plt.rcParams['font.sans-serif'] = 'SimHei'
        plt.title('生命游戏与matplotlib散点图')

        running = True
        plt.ion()  # 打开交互模式
        while running:
            x_list = []  # 散点图的x轴坐标点列表
            y_list = []  # 散点图的y轴坐标点列表
            self.copy_a = self.next_array(self.copy_a)  # 调用next_array()方法计算下一个数组
            for x in range(self.X_DOT):
                for y in range(self.Y_DOT):
                    if self.source_a[x, y]:  # 如果满足细胞存活条件：
                        x_list.append(x)  # 将x添加到x轴列表里
                        y_list.append(y)  # 将y添加到y轴列表里
            plt.scatter(x_list, y_list)  # 画出所有存活细胞的散点图
            plt.pause(0.5)  # 间歇时间0.5s
            self.source_a = np.copy(self.copy_a)
            plt.clf()  # 清空画布
            # fig2.add_subplot(111)
        plt.ioff()

if __name__ == '__main__':
    LiveGame(50,50).main()

