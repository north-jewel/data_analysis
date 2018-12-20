from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS

def image(file_txt,mask_png,new_name_png):
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    text = open(path.join(d, file_txt),encoding='utf-8').read()
    alice_mask = np.array(Image.open(path.join(d, mask_png)))
    stopwords = set(STOPWORDS)
    stopwords.add("said")
    wc = WordCloud(font_path='./fonts/simhei.ttf',background_color="white", max_words=2000, mask=alice_mask,
                   stopwords=stopwords, contour_width=3, contour_color='steelblue')
    wc.generate(text)
    dd = r'C:\Users\XIAOMI\Desktop\GiTHub\Day2\wordcloud\my\My\analyze\computer_test\create'
    wc.to_file(path.join(dd, new_name_png))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.show()

welfare = 'company_welfare.txt'
required = 'experience_required.txt'
job_requir = 'job_required.txt'
work = 'work_require.txt'
ali_co = 'alice_color.png'
alc_ma = 'alice_mask.png'
stor = 'stormtrooper_mask.png'

image(work,ali_co,'work_requir.png')

import pandas as pd

def aa(min,max):
    start = int(min*10)
    end = int(max*10+1)
    list = [i for i in range(start,end,1)]
    return list

sal_list = []
'''
with open('end_info_3.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    a = 1
    c = 1
    head = True
    for dic in lines:
        dic = eval(dic)
        if dic['city'].startswith('北京'):
            salary = dic['salary']
            if salary:
                if '年' in salary or '天'in salary or '小时' in salary:
                    pass
                else:
                    # print(a)
                    if '-' in salary:
                        min_ind = salary.index('-')
                        if '千' in salary:
                            max_ind = salary.index('千')
                            min_sal = float(salary[:min_ind])*0.1
                            max_sal = float(salary[min_ind+1:max_ind])*0.1
                            list_ = aa(min_sal,max_sal)
                            sal_list.extend(list_)
                            a += 1
                        else:
                            max_ind = salary.index('万')
                            min_sal = float(salary[:min_ind])
                            max_sal = float(salary[min_ind+1:max_ind])
                            list_ = aa(min_sal,max_sal)
                            sal_list.extend(list_)
                            a += 1
                    else:
                        if '千' in salary:
                            min_ind = salary.index('千')
                            sal = float(salary[:min_ind])*0.1
                            list_ = aa(0,sal)
                            sal_list.append(list_)
                            a+=1
                        else:
                            min_ind = salary.index('万')
                            sal = float(salary[:min_ind])
                            list_ = aa(0,sal)
                            sal_list.append(list_)
                            a+=1
nd = np.array(sal_list)
aa = np.bincount(nd)
print(len(aa))
'''
