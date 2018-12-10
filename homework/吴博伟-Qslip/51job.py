import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import wordcloud
import re
from wordcloud import WordCloud, STOPWORDS
from matplotlib.pyplot import savefig
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 公司一般会提供什么福利诱惑?

df = pd.read_csv('51jobs.csv')
df = df.dropna(how='any')
df.head()
df2 = df.welfare.values

text = open('51jobs.txt',encoding='utf-8').read()
x, y = np.ogrid[:1200, :1200]

mask = (x - 600) ** 2 + (y - 500) ** 2 > 520 ** 2
mask = 255 * mask.astype(int)


wc = WordCloud(background_color="white", 
               repeat=True, mask=mask,
               font_path=r'C:\Windows\Fonts\simkai.ttf'
              ,mode="RGBA" )
wc.generate(text)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
savefig(r'C:\Users\48170\Desktop\51jobs.png',dpi=600)
plt.show()
