import requests
from bs4 import BeautifulSoup
import time
from 前程无忧_1 import AnalyzerCatalog
from 前程无忧 import Analyzer
import pandas as pd

#查看总页数
# res = requests.get('https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html')
# res.encoding = 'gbk'
# html = res.text
# soup = BeautifulSoup(html, 'html.parser')
# page = soup.select_one('span.td').text.replace('共','').replace('页，到第','')
for i in range(1,100):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html'.format(i)
    a = AnalyzerCatalog(url).all_url()
    info = []
    for i in a:
        if 'https://jobs.51job.com' in i:
            b = Analyzer(i).info()
            if b == None:
                pass
            else:
                info.append(b)
                print(b)
                time.sleep(1)
        else:
            pass
    columns = ['城市', '技术类型', '公司名', '公司大小', '公司类型', '公司简介', '公司位置', '职位要求', '学历需求', '经验要求', '公司福利']
    df = pd.DataFrame(info, columns=columns)
    df.to_csv('爬虫.csv', mode='a', encoding="utf_8_sig", index=False)
    time.sleep(1)

# i = 0
# while True:
#     if i < int(page):
#         try:
#             print(i+1)
#             url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html'.format(i+1)
#             a = AnalyzerCatalog(url).all_url()
#             print(len(a))
#         except:
#             print(i+1)
#             url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html'.format(i + 1)
#             a = AnalyzerCatalog(url).all_url()
#             print(len(a))
#             with open('url.txt', 'a') as f:
#                 for x in a:
#                     f.write(x)
#                     f.write('\n')
#             i += 1
#             time.sleep(1)
#         else:
#             with open('url.txt', 'a') as f:
#                 for x in a:
#                     f.write(x)
#                     f.write('\n')
#             i += 1
#             time.sleep(1)
