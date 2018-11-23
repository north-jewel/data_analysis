import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
width=50
hight=50
np.random.seed(2)
start=np.random.randint(0,2,(width,hight))

def mothod(x,y):
    counts = 0
    for i in (x + 1, x, x - 1):
        for j in (y + 1, y, y - 1):
            if i == x and j == y:
                continue
            if i < 0 or i > width - 1 or j < 0 or j > width - 1:
                continue
            if start[i][j]:
                counts += 1
    #print(counts)
    return counts
#mothod(5,6)

def pl(start):
    xy=start.copy()
    for i in range(width):
        for j in range(hight):
            counts=mothod(i,j)
                #print(counts)
            if counts==3:
                    
                xy[i][j]=1
                    #y.append(f)
            if counts == 2:
                pass
                    #y.append(j)
            else:
                xy[i][j]=0
    #print(xy)
    return xy



def f(xy):
    x=[]
    y=[]
    for i in range(width):
        for j in range(hight):
            if xy[i][j]:
                x.append(i)
                y.append(j)
    return x,y
def a(arg):
    return np.array(arg)
    
while True:
    xy=pl(start)
    start=xy
    #print(xy)
    x,y=f(xy)
    x=a(x)
    y=a(y)
    plt.grid()
    plt.scatter(x,y)
    plt.show()
    
    #time.sleep(5)
# print(x)
# print(y)

