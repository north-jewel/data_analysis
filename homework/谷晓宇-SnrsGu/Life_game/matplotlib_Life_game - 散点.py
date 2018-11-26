import numpy as np,matplotlib.pyplot as plt

class Life_game:
    def __init__(self,number):
        self.number = number
        self.ndarray = np.random.randint(0,2,(number,number))
        self.game()

    def initial(self,numpy):
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
            for x in range(self.number):
                for y in range(self.number):
                    if self.ndarray[x, y]:
                        plt.scatter(x, y, s=30,c = 'b',alpha=.5)
            plt.ioff()
            plt.pause(0.03)
            nuw = self.initial(self.ndarray)
            self.ndarray = nuw


if __name__ == '__main__':
    x = Life_game(50)
