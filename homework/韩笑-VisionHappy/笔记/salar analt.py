import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
def xinzi ():
    df = pd.read_csv(r'wcwy.csv', encoding='gbk')

    salary_s = df['salary']
    salary_s.dropna(inplace=True)
    wan_per_month = salary_s[salary_s.str.contains('万/月')]
    wan_per_month=wan_per_month.str.replace('万/月','')
    wan_per_month = wan_per_month.str.split('-')
    wan_per_month__mean = wan_per_month.apply(lambda x:(float(x[0])+float(x[1]))/2)
    wan_per_month__mean_d = wan_per_month__mean[wan_per_month__mean<30]

    print(wan_per_month__mean_d)
    plt.plot(wan_per_month__mean_d)
    plt.show()

xinzi()