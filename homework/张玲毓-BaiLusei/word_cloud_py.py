from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
class Picture:
    def produce_picture(self,text):
# filename = r'D:\Learn\Notebook\demo\end_info.csv'
# filetext = r'D:\Learn\Notebook\demo\company_welfare.txt'

# df = pd.read_csv(filename,encoding='utf-8')
# print(df)
# text = list(df['company_welfare'])
# print(text)
# print(type(text))
        wd = WordCloud(background_color="white", max_words=3000,font_path='./fonts/simhei.ttf',contour_width=10)
        wd.generate(text)
        plt.imshow(wd,interpolation = 'bilinear')
        plt.axis('o,ff')
        wd.to_file('company_welfare.jpg')
        plt.show()
if __name__ == '__main__':
    text = open(path.join(d, 'company_welfare.txt'),encoding='utf-8').read()
    a = Picture()
    a.produce_picture(text)