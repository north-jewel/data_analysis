import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


data = {'brain':np.random.randint(2,250,10),'mobile':np.random.randint(2,10,10),
        'shadow':np.random.randint(2, 10, 10),'sill' : np.random.randint(2,10,10),
        'rule':np.random.randint(2, 10, 10),
        'all_class':['1802c','1803c','1804c','1805c','1806c','1807c','1808c','1809c','1803a','1804a']}

def jishi(data):
    fig, ax = plt.subplots()
    x = np.arange(10)
    plt.title('9-25-10.25月度违纪对比')
    plt.ylim(0,300)
    plt.xticks(x,data['all_class'])
    plt.bar(x,data['brain'],label='电脑')
    plt.bar(x,data['mobile'],bottom=data['brain'],label='手机')
    plt.bar(x,data['sill'],bottom=data['brain']+data['mobile'],label='未关窗')
    plt.bar(x,data['shadow'],bottom=data['brain']+data['mobile']+data['sill'],label='投影')
    plt.bar(x,data['rule'],bottom=data['brain']+data['mobile']+data['sill']+data['shadow'],label='违纪')
    plt.legend(loc = 'upper left')
    plt.show()

jishi(data)
