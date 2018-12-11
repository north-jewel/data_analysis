import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import pylab as pl

plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号
plt.figure(figsize = (10,5))
df = pd.read_csv('beijing_zhaopin_data.csv',encoding = 'gbk')
df2 = df.groupby(by = 'company_site').count()
data_list = []
for i in df2.index:
    if i[:2] == '北京':
        data_list.append(i)
#data_list
df3 = df[df.company_site.isin(data_list)]
df4 = df3.groupby(by = 'company_site').count()
# y = df4[df4.title > 50]
y = df4.iloc[1:]
x = np.arange(len(y.index))
plt.title('北京一些地区提供的岗位')
plt.xticks(x,y.index)
plt.bar(x,y.title)
pl.xticks(rotation=70)

savefig('images\工作数量.png')
plt.show()
