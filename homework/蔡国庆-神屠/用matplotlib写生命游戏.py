import numpy as np
import matplotlib.pyplot as plt
class Life_Game():
    def __init__(self,number):
        self.number = number
        self.array = np.random.randint(0,2,(number,number))
        self.copy = self.array.copy()
    def judge(self,x,y):
        counts = 0
        for i in (x - 1, x, x + 1):
            for j in (y - 1, y, y + 1):
                if i == x and j == y:
                    continue
                if i < 0 or j < 0 or i >= self.number or j >= self.number:
                    continue
                if self.array[i][j] == 1:
                    counts += 1
        return counts
    def live_or_die(self,counts,x,y):
        # plan = []
        # for x in range(numpy.shape[0]):
        #     for y in range(numpy.shape[1]):
        #         life = self.judge(x,y)
        #         if life == 3:
        #             plan.append((x,y,1))
        #         elif life == 2:
        #             pass
        #         else:
        #             plan.append((x,y,0))
        # for i in plan:
        #     numpy[i[0]][i[1]] = i[2]
        if counts == 2:
            return self.array[x,y]
        if counts > 3 or counts < 2:
            return 0
        if counts == 3:
            return 1
    def next_a(self,array):
        for x in range(self.number):
            for y in range(self.number):
                result = self.live_or_die(self.judge(x,y),x,y)
                array[x,y] = result
        return array
    def game(self):
        while True:
            
            x_list = []
            y_list = []
            self.copy = self.next_a(self.copy)
            for x in range(self.number):
                for y in range(self.number):
                    if self.array[x,y] == 1:
                        x_list.append(x)
                        #print(list_x)
                        y_list.append(y)

            plt.ioff()
            plt.scatter(x_list, y_list, c='blue')
            plt.pause(0.3)
            self.array = self.copy.copy()
            plt.clf()#  清空画布
if __name__ == '__main__':
    x = Life_Game(10).game()










                        
        
