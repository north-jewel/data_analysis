import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = {'brain':np.random.randint(2,250,10),'mobile':np.random.randint(2,10,10),
        'shadow':np.random.randint(2, 10, 10),'sill' : np.random.randint(2,10,10),
        'rule':np.random.randint(2, 10, 10)}
all_class = ['1802c','1803c','1804c','1805c','1806c','1807c','1808c','1809c',
                     '1803a','1804a']
df = pd.DataFrame(data,index=all_class)
def jishi():
    fig1, ax1 = plt.subplots()
    plt.title('1802c班违纪情况')
    plt.ylim(0,45)
    plt.grid(axis='y')
    x = np.arange(5)
    plt.xticks(x,['未带电脑总数','未带手机总数','未关投影','未关窗','违纪'])
    plt.bar(x,df.loc['1802c'])
    plt.annotate('数量:{}'.format(df.loc['1802c'][0]),color='b',xy=(0,40),xytext=(1,40),arrowprops=dict(facecolor='red',
                arrowstyle="->", connectionstyle="angle"),
                )
    plt.annotate('数量:{}'.format(df.loc['1802c'][1]),color='b',xy=(1,5),xytext=(1,10),arrowprops=dict(facecolor='red',
                arrowstyle="->", connectionstyle="angle"),
                )
    plt.annotate('数量:{}'.format(df.loc['1802c'][2]),color='b',xy=(2,5),xytext=(2,10),arrowprops=dict(facecolor='red',
                arrowstyle="->", connectionstyle="angle"),
                )
    plt.annotate('数量:{}'.format(df.loc['1802c'][3]),color='b',xy=(3,5),xytext=(3,10),arrowprops=dict(facecolor='red',
                arrowstyle="->", connectionstyle="angle"),
                )
    plt.annotate('数量:{}'.format(df.loc['1802c'][4]),color='b',xy=(4,5),xytext=(4,10),arrowprops=dict(facecolor='red',
                arrowstyle="->", connectionstyle="angle"),
                )
    plt.show()
jishi()
