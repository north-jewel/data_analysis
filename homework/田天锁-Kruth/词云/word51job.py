"""

@author:tts

@file: word51job.py

@time: 2018/12/07

"""
import numpy as np
from os import  path
from  PIL import  Image
from wordcloud import  WordCloud,STOPWORDS
import  matplotlib.pyplot as plt

d = path.dirname(__file__)
#读取文本
text = open(path.join(d, 'end_info.txt'),encoding='utf-8').read()

#读取图片
alice_mask = np.array(Image.open(path.join(d,'23.jpg')))

sts= set(STOPWORDS)
sts.add('said')
#设置词云的一些属性
wc = WordCloud(font_path='./fonts/simhei.ttf',background_color='white',max_words=2000,mask=alice_mask,
               stopwords=sts)

#生成词云
wc.generate(text)

#保存到本地
wc.to_file(path.join(d,'alice.png'))

#展示
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.figure()
plt.imshow(alice_mask,cmap = plt.cm.gray,interpolation='bilinear')
plt.axis('off')
plt.show()