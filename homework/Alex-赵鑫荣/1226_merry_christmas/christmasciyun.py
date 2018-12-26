# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Project:      python4
# Name:         christmasciyun
# Description:  PyCharm
# Author:       ZXR
# Date:         2018/12/26
# Time:         7:49
#-------------------------------------------------------------------------------

from PIL import Image
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# img = Image.open(r'c:\users\zxr\desktop\640.png')
# img = img.convert('L')
# img.save('灰度图.jpg')

# img = img.convert('1')
# img.save('二值图.jpg')

df = pd.read_csv(r'E:\python4\lagou1124pro\qcwy.csv')
t = df['work_fare'].dropna()

t_list = []
for x in t:
    t_list.extend(x.split('\r\n'))
text = ''
for t in t_list:
    text += t+','
c = '圣诞快乐,'
c = c*1000
# print(text)
text += c
print(text)
img = Image.open(r'c:\users\zxr\desktop\timg.jfif')
chri_coloring = np.array(img)
stopwords = set(STOPWORDS)
stopwords.add('said')
wc = WordCloud(background_color= 'white',max_words = 2000,
               mask = chri_coloring,stopwords = stopwords,
               max_font_size=40,random_state = 42,font_path='C:\windows\Fonts\STZHONGS.TTF')

wc.generate(text)
image_colors = ImageColorGenerator(chri_coloring)

fig,axes = plt.subplots(1,3,figsize = (20,20))
axes[0].imshow(wc,interpolation = 'bilinear')
axes[1].imshow(wc.recolor(color_func = image_colors),interpolation = 'bilinear')
axes[2].imshow(chri_coloring,cmap = plt.cm.gray,interpolation = 'bilinear')

for ax in axes:
    ax.set_axis_off()
plt.show()
plt.savefig('christmas2.png')
