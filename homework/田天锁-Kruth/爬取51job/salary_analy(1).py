# 1.薪资分布?

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

def add_dict(df, dict):
    df = df.append(dict, ignore_index=True)
    return df

# txt --> df -->excel
def readtxt2df(txt_file_path, df):
    excel_file = None
    df1 = df
    with open(txt_file_path, encoding='utf-8') as f:
        has_content = True
        while has_content:
            try:
                has_content = f.readline()
                # 一个dict = 一条数据 = df中的一行
                dict1 = json.loads(has_content)

                df1 = add_dict(df1,dict1)
            except Exception as e:
                print('有空值..')
        return df1




    return excel_file


# readtxt2df('end_info.txt',None)
dict1 = {"skill_type": "Python实习-机器学习方向", "city": "北京-朝阳区", "company_name": "寰宇优才教育科技（北京）有限公司",
         "company_size": "150-500人", "company_type": "计算机软件", "company_description": "寰宇优才教育科技（北京）有限公司",
         "company_location": "上班地址:新文化大街", "salary": "0.8-1万/月",
         "job_required": "(能力不足,但有Python开发意向者,可放宽要求提供实习岗位)"
                         "1.本科以上学历,有良好的数学基础和逻辑建模能力;"
                         "2.深入理解诸如回归、分类、聚类等机器学习领域的基本概念;"
                         "3.熟悉推荐引擎、自然语言处理、语音识别、图像识别、人脸识别、神经网络等人工智能领域的相关算法;"
                         "4.熟练掌握Python语言;"
                         "5.熟练使用Numpy、Scipy、Matplotlib、Pandas等数值计算库;"
                         "6.熟练使用sklearn、nlp、opencv等机器学习工具包;"
                         "7.具有一定的深度学习研发背景,熟悉至少一种深度学习框架,如:TensorFlow、Caffe、Theano、Keras、ConvNet、Torch等;"
                         "8.在至少一个领域有深入的研究,如:深度神经网络、语义分析、模式识别、机器视觉、量化金融等;"
                         "9.在强化学习领域有丰富的项目经验及算法实现能力者优先考虑;"
                         "10.善于分析问题、解决问题,具备丰富的想象力、卓越的学习能力和创造性思维能力,具有良好的团队协作精神,怀有推动人工智能不断发展的理想和使命感.",
         "experience_required": "无工作经验",
         "company_welfare": "五险一金\n补充医疗保险\n补充公积金\n员工旅游\n交通补贴\n出国机会\n年终奖金\n绩效奖金\n定期体检\n弹性工作"}

# df = pd.DataFrame.from_dict(dict1,orient='index').T
# df = pd.DataFrame.from_dict(dict1,orient='index').T
# df.drop(0,inplace=True)
df = pd.DataFrame(columns=dict1.keys())
# print(df)


# df = readtxt2df('text.txt',df)
# df.to_excel('end_info.xls')
# df.to_csv('text.csv',index=False,encoding='gbk')
# df = readtxt2df('end_info.txt', df)
# df.to_csv('end_info.csv',index=False)
# print(df)

# 薪资分布?   salary
end_info = 'end_info.csv'
text = 'text.csv'
df = pd.read_csv(end_info)
# print(type(df.salary))
# print(df.salary)

s1 = pd.Series([1,12,3])
# s1.str.

# print(df.salary.str.contains('万/月'))
print('********')
# 处理空值
salary_s = df.salary
salary_s.dropna(inplace=True)
print('去除空值之后的salary_s:',salary_s)

wan_per_month = salary_s[salary_s.str.contains('万/月')]
print(len(wan_per_month))
print(wan_per_month)  # 4675

# wan_per_year = salary_s[salary_s.str.contains('万/年')]
# print(len(wan_per_year))
# print(wan_per_year)  # 197
# print('*********')
# yuan_per_day = salary_s[salary_s.str.contains('元/天')]
# print(len(yuan_per_day))
# print(yuan_per_day)  # 45

# 万/年 的情况, 所占比重不大, 我们此处选择不考虑

wan_per_month = wan_per_month.str.replace('万/月','')
wan_per_month = wan_per_month.str.split('-')
wan_per_month_mean = wan_per_month.apply(lambda x:(float(x[0])+float(x[1]))/2)
# print(wan_per_month)
# print(type(wan_per_month))
# print(wan_per_month.dtypes)
# print(wan_per_month_mean)
# print(type(wan_per_month_mean))

# 随便画个图来感受一下数据,看看有没有 离群值
# 离群值,和咱们的期望相差比较大的值

# wan_per_month_mean.plot()
# plt.show()


# 根据一个series 画图
def myplot(s1):
    df = s1.to_frame()
    column = df.columns[0]
    df['index'] = df.index.tolist()
    df.plot.scatter(x='index', y=column)
    plt.show()

# 再清洗一下, 去除 离群值, >10 的去掉
#  10 这个阈值是根据观察得来的
#  6-10 阈值都是可以的,根据自己的经验

wan_per_month_mean_d = wan_per_month_mean[wan_per_month_mean<10]

# myplot(wan_per_month_mean_d)

#  hist  patches



def salary_plot(salary_s):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    n, bins, patches = plt.hist(salary_s, 20, facecolor='g', alpha=0.5)
    plt.xlabel('薪酬,万元/月')
    plt.ylabel('人数')
    plt.title('薪资结构')
    plt.show()
# 绘制薪资分布图
# salary_plot(wan_per_month_mean_d)


# ----------------- 薪资和地区关系图 --------------------

print(type(df.city))
print(len(df.city))

print(df.city.isnull().sum())

# print(len(df.groupby(by='city').groups))

# 找一个 北京地区的 list,
# list中每个元素都包含 '北京' 两字

print(df.city[df.city.str.contains('北京')])

df_bj = df[df.city.str.contains('北京')]
df_bj = df_bj[df_bj.salary.notnull()]

#  "salary": "0.8-1万/月",
# 只取 万元/月
df_bj = df_bj[df_bj.salary.str.contains('万/月')]
df_bj.salary = df_bj.salary.str.replace('万/月','')
df_bj.salary = df_bj.salary.str.split('-')
df_bj['new_salary'] = df_bj.salary.apply(lambda x:(float(x[0])+float(x[1]))/2)
df_bj = df_bj[df_bj.new_salary<10]
print(len(df_bj))
print(df_bj)
print('df_bj shape',df_bj.shape)

## 各个地区的平均工资分布图
# print(df_bj.groupby(by='city').agg('mean'))
# salary_city = df_bj.groupby(by='city').agg('mean')
# salary_city.plot()
# plt.show()

# 不同地区 提供的岗位 数量图
print(df_bj.groupby(by='city').agg('count')['new_salary'])
salary_city = df_bj.groupby(by='city').agg('count')['new_salary']
print(type(salary_city))
print(salary_city.index)
salary_city.plot(use_index=True)

plt.show()

# print(df_bj.groupby(by='city').agg('count'))
# salary_city = df_bj.groupby(by='city').agg('count')
# salary_city.plot()
# plt.show()