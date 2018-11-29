import pandas as pd
from pylab import *

def Test_2(age,date):
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    index = age.shape
    X = np.arange(index[1]) + 1
    color = ['steelblue','coral','darkgrey','gold','red']
    label = ['未带电脑总数','未带手机总数','未关投影仪总数次数','未关门窗次数','校查违纪']
    plt.xticks(X,age.columns)
    for i in range(index[0]):
        plt.bar(X,age.iloc[i],width = 0.7,color = color[i],bottom = np.sum(age.iloc[:i]),label = label[i])
    ax = plt.gca()
    for i in ax.spines:
        ax.spines[i].set_color('none')
    ax.yaxis.grid(True)
    plt.ylim(0, 300)
    plt.legend(bbox_to_anchor = (0,-0.2,1,0.1),ncol = 5,mode = 'expand',loc='upper right')
    plt.title(date+'月度违纪对比')
    plt.show()
    return plt

class_list = ['1802C','1803C','1804C','1805C','1806C1','1806C2','1807C1','1807C2','1808C1','1808C2']
info_list = [[45,5,0,0,3],[250,5,0,0,3],[40,1,0,1,2],[25,3,0,1,5],[10,0,0,0,3],[2,0,0,0,2],[75,0,0,0,4],[80,0,0,3,8],[6,0,0,1,1],[15,0,0,0,3]]
info = pd.DataFrame(dict(zip(class_list,info_list)))
date = '9.25-10.25'
Test_2(info,date)