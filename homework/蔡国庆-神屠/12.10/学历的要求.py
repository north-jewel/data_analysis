import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号

df = pd.read_csv('beijing_zhaopin_data.csv',encoding='gbk')
df1 = df.groupby(['edu_required']).count()
df1.title.sort_values()
education_list = []
for i in df1.index:
    if i[0] != '招':
        education_list.append(i)
df2 = df[df.edu_required.isin(education_list)]
education_data = df2.groupby('edu_required').count()
x = np.arange(len(education_data.index))
plt.xticks(x,education_data.index)
plt.title('北京一些找工作的学历要求')
plt.bar(x,education_data.title)
for a,b in zip(list(x),list(education_data.title.values)):
    plt.annotate(b, xy=(a,b), xytext=(0.4, 30),textcoords = 'offset points',arrowprops=dict(facecolor='w', shrink=0.06))
savefig('images\学历要求')
plt.show()