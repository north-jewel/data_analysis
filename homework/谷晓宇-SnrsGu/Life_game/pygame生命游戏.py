import numpy as np
import pygame

class Life_game:
    def __init__(self,x_dot,y_dot,dot_px = 10):
        self.x_dot = x_dot
        self.y_dot = y_dot
        self.dot_px = dot_px
        self.ndarray = np.random.randint(0,2,(x_dot,y_dot))
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
                if i < 0 or i > self.x_dot-1 or j < 0 or j > self.y_dot-1:
                    continue
                if self.ndarray[i][j]:
                    counts += 1
        return counts

    def game(self):
        pygame.init()
        pygame.display.set_caption("SnrsGu-Life_game")
        screen = pygame.display.set_mode((self.dot_px * self.x_dot,self.dot_px * self.y_dot))
        running = True
        while running:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for x in range(self.x_dot):
                for y in range(self.y_dot):
                    if self.ndarray[x,y]:
                        screen.fill((0,0,255),(y * self.dot_px,x * self.dot_px,self.dot_px,self.dot_px))
                        pygame.draw.rect(screen,(0,0,0),(y * self.dot_px,x * self.dot_px,self.dot_px,self.dot_px),1)
            pygame.display.update()
            nuw = self.initial(self.ndarray)
            self.ndarray = nuw
            #pygame.time.wait(0)

if __name__ == '__main__':
    x = Life_game(50,50,10)
