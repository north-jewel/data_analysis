import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('info.csv')
print(df.head())
print(df.Officialprice)
def str_(str_):
    str_=str_.replace('万','')
    str1=str_.split('-')
    print(str1)
    if len(str1) > 1:
        return float(str1[1])
    elif len(str1) == 1:
        return float(str1[0])
    else:
        return float(str1)
df['top_price']=df.Officialprice.apply(str_)
print('最贵的车排行前五')
print(df.sort_values(by='top_price',ascending=False).head())


def displace(str_,mothod=True):
    a=[]
    str1 =str_.split(', ')
    # print(str1)
    for i in str1:
        i=i.replace('L','').replace('\'','').replace('纯电动','').replace('T','').replace('--','')
        if len(i) != 0:
            a.append(float(i))
        # print(type(float(i)))

    if mothod:
        if len(a):
            max_=max(a)
            return max_

    else:
        if len(a):
            min_=min(a)
            return min_
# print(df.groupby(by='Displacement').count())

print('大排量前五')
df['max_displace']=df.Displacement.apply(displace)
df_d=df.sort_values(by='max_displace',ascending=False)
print(df_d.head())
# print(new_df.sort_values(by='max_displace',ascending=False).tail())
# print(df['Displacement'].head(1))
# print(new_df.Displacement)
print('小排量前五')
print(df.sort_values(by='max_displace',ascending=True).dropna().head())
print('评价优秀的车')
print(df[df['Price'] == '优秀'])
print('什么档 最多')
print(df.groupby(by='Gearbox').count().sort_values(by='Price',ascending=False).head())