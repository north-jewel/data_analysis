from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

plt.figure(figsize=(15, 10))
df = pd.read_csv('beijing_zhaopin_data.csv', encoding='gbk')
df1 = df['job_info']

df1.to_csv('txt\工作技能.txt')
text = open('txt\工作技能.txt', encoding='utf-8').read()
text = text.replace('xa0', '').replace('\\n', '').replace('\\t', '').replace('岗位职责', '').replace('任职要求', '').replace(
    '工作职责', '').replace('任职资格', '').replace('岗位要求', '').replace('职能类别', '').replace('职位要求', '').replace('职位描述', '').replace(
    'r', '').replace('算法工程师','').replace('本科以上学历','').replace('软件工程师','').replace('本科及以上学历','')
wc = WordCloud(font_path='./fonts/simhei.ttf', background_color="white", width=800, height=400)
wc.generate(text)
wc.to_file('images\工作技能.png')  # 字体越大则说明这项福利大多数公司都有
plt.title('应聘时需要会的技能')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()