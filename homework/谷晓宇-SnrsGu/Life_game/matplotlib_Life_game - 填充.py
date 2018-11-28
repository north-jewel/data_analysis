import numpy as np,matplotlib.pyplot as plt

class Life_game:
    def __init__(self,number):
        self.number = number
        self.ndarray = np.random.randint(0,2,(number,number))
        self.game()

    def initial(self,numpy):
        '''

        :param numpy: 上一个数组
        :return: 根据规则判断后的一个新的数组
        '''
        plan = []
        for x in range(numpy.shape[0]):
            for y in range(numpy.shape[1]):
                life = self.has_counts(x,y)
                if life == 3:
                    plan.append((x,y,1))
                elif life == 2:
                    pass
                else:
                    plan.append((x,y,0))
        for i in plan:
            numpy[i[0]][i[1]] = i[2]
        return numpy

    def has_counts(self,x,y):
        '''

        :param x: x轴坐标
        :param y: y轴坐标
        :return: 返回该点周围存活生命的个数
        '''
        counts = 0
        for i in (x+1,x,x-1):
            for j in (y+1,y,y-1):
                if i == x and j == y:
                    continue
                if i < 0 or i > self.number - 1 or j < 0 or j > self.number - 1:
                    continue
                if self.ndarray[i][j]:
                    counts += 1
        return counts

    def game(self):
        plt.ion()
        while True:
            plt.cla()
            for i in range(self.number + 1):
                plt.plot([0, self.number], [i, i], 'black')
                plt.plot([i, i], [0, self.number], 'black')
            for x in range(self.number):
                for y in range(self.number):
                    if self.ndarray[x, y]:
                        plt.fill_between([x, x + 1], [y + 1], [y], facecolor='r')
            plt.ioff()
            plt.pause(0.03)
            nuw = self.initial(self.ndarray)
            self.ndarray = nuw


if __name__ == '__main__':
    x = Life_game(50)
