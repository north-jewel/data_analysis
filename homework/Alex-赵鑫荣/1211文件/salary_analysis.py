# -*- coding: utf-8 -*-
"""
   File Name：     salary_analysis
   Product:        PyCharm
   Project:    python4
   File:       salary_analysis.py
   Author :       ZXR
   date：          2018/12/11
   time:           9:37
"""
import pandas as pd
import json
import matplotlib.pyplot as plt

d1 = pd.DataFrame(columns = ['skill_type','city','company_name','company_size',
                             'company_type','company_description','company_location',
                             'salary','job_required','experience_required','company_welfare'])

def add_dataframe(d1,d2):
    '''
    通过传入两个DataFrame，将第二个DataFrame追加到第一个DataFrame中，并返回添加后的DataFrame
    :param d1: 第一个DataFrame
    :param d2: 第二个DataFrame(或者dict_like)
    :return: 返回添加后的DataFrame
    '''
    df_added = d1.append(d2,ignore_index = True)
    return df_added

def read_txt(file_path,d1):
    '''
    打开文本文件，并逐行读取、然后追加到一个DataFrame中，最后返回这个DataFrame
    :param file_path: 文本文件路径
    :param d1: 一个空的DataFrame
    :return: 返回一个追加后的DataFrame
    '''
    with open(file_path,'r',encoding = 'utf-8') as f:
        content = True
        while content:
            content = f.readline()
            try:
                d2 = json.loads(content)
            except Exception as e:
                print(e)
            else:
                d1 = add_dataframe(d1,d2)
                # d1 = d1.append(d2,ignore_index=True)
        return d1

#逐行读取文本文件并逐行累计添加到一个DataFrame中，返回这个DataFrame
# df = read_txt(file_path=r'E:\python4\1211OfDataFrame\end_info.txt',d1=d1)
# print(len(df))
# print(df)

#将DataFrame写入CSV文件
# df.to_csv('end_info.csv',index = False,encoding = 'utf-8')

df = pd.read_csv('end_info.csv',encoding = 'utf-8')
print(len(df))
salary_s = df['salary']
print(len(salary_s))
salary_s.dropna(inplace = True)
# print('去除空值后的工资一列数据：\n',salary_s)
print(len(salary_s))


#索引出 万/月 的数据
wan_salary = salary_s[salary_s.str.contains('万/月')]
print(len(wan_salary))
#索引出 千/月 的数据
qian_salary = salary_s[salary_s.str.contains('千/月')]
print(len(qian_salary))

#将 万/月 从每一项中去掉
wan_salary_replace = wan_salary.str.replace('万/月','')
#然后再按照'-'进行切开，返回一个列表
wan_salary_split = wan_salary_replace.str.split('-')
# print(wan_salary_split)
#求出每一项的平均值
wan_salary_mean = wan_salary_split.apply(lambda x:(float(x[0])+float(x[1]))/2)
print(wan_salary_mean)

#先画个图展示一下数据的大概情况，
# wan_salary_mean.plot()
# plt.show()

def myplot(s1):
    df = s1.to_frame()
    column = df.columns[0]
    df['index'] = df.index.tolist()
    df.plot.scatter(x = 'index',y = column)
    plt.show()

#再清洗一下，去除离群值
wan_salary_lt10 = wan_salary_mean[wan_salary_mean<10]
# myplot(wan_salary_lt10)

def salary_plot(salary_series):
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    n,bins,patches = plt.hist(salary_series,20,facecolor = 'r',alpha = 0.5)
    plt.xlabel('工资(单位：万/月)')
    plt.ylabel('频数')
    plt.title('工资分布图')
    plt.show()

#绘制工资分布图
# salary_plot(wan_salary_lt10)


#  --------薪资和地区关系图------
print(df.city.isnull().sum())
print(len(df))
df_bj = df[df.city.str.contains('北京')]
print(len(df_bj))
df_bj = df_bj[df_bj.salary.notnull()]
print(len(df_bj))

df_bj = df_bj[df_bj.salary.str.contains('万/月')]
df_bj.salary = df_bj.salary.str.replace('万/月','')
df_bj.salary = df_bj.salary.str.split('-')
df_bj['new_salary'] = df_bj.salary.apply(lambda x:(float(x[0])+float(x[1]))/2)
df_bj = df_bj[df_bj.new_salary<10]
print(len(df_bj))
print(df_bj.shape)

#各个地区的平均工资分布图
df_bj_mean = df_bj.groupby('city').agg('mean')
print(df_bj_mean.index)
# df_bj_mean.plot()
#画出各地区平均工资分布图
plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.plot(df_bj_mean.index,df_bj_mean.values)

#    不同地区提供的岗位数量图
# count_city = df_bj.groupby("city").agg('count')['company_name']
# print(count_city)
count_city = df_bj['city'].value_counts()
print(count_city)
# count_city.plot(use_index = True)
#画出通过地区分组后 每组工资一列的个数
plt.plot(count_city.index,count_city.values)

