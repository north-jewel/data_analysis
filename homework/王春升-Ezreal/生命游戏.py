"""

@author:tts

@file: games.py

@time: 2018/11/12

"""
import matplotlib.pyplot as plt
import random
l=[[random.choice((0,1)) for i in range(10)] for i in range(10)]
k=[[0 for i in range(10)] for i in range(10)]

def z(x,y):
 m=0
 for i in (x-1,x,x+1):
  for j in (y-1,y,y+1):
   if i==x and y==j:
    continue
   if (i<0 or i>9 or j<0 or j>9):
    continue
   if (l[i][j]):
    m+=1
 return m
import copy
def a():
  #plt.imshow()   
 for x in range(10):
  for y in range(10):
   m=z(x, y)
   if m==2:
    k[x][y]=l[x][y]
   elif m==3:
    k[x][y]=1
   else:
    k[x][y]=0
while True:
    plt.imshow(l)
    a()
    plt.pause(0.2)
    plt.ioff()
    l=copy.deepcopy(k)
