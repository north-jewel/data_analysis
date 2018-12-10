from os import path
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import jieba
from wordcloud import WordCloud, STOPWORDS

def write_csv_(key):
    with open('xx.txt','w',encoding= 'gbk')as f:
        data = pd.read_csv('qiancheng_data.csv',encoding='gbk')
        data = data.dropna()
        data_1 = data[key]
        if key == 'company_site':
            data_2 = data_1.tolist()
            for i in data_2:
                x = i.strip('北京-')
                f.write(x)

        else:
            data_2 = data_1.tolist()
            for i in data_2:
                f.write(i+',')


list_1 = ['salary','company_site','experience_required','company_welfare','edu_required']

for x in list_1:
    write_csv_(x)
    open_text = open('xx.txt',encoding='gbk').read()
    wordcloud = WordCloud(font_path='./fonts/simhei.ttf',max_font_size=66).generate(open_text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()




