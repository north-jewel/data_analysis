import requests
import re
import numpy as np
import pandas as pd
import urllib
from bs4 import BeautifulSoup


def url_list():
    with open(r'C:\Users\20312\Desktop\qc1.txt', 'w') as f:
        for i in range(1,31):
            #url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,' \
             #     'Python%2520%25E9%25AB%2598%25E7%25BA%25A7,2,{}.html?lang=c&stype=' \
             #     '&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99' \
               #   '&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0' \
                #  '&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(i)

            url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,' \
                  'Python%2B%25E9%25AB%2598%25E7%25BA%25A7,2,{}.html?lang=c&stype=2&postchannel=0000' \
                  '&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0' \
                  '&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=' \
                  '&specialarea=00&from=&welfare='.format(i)
            info = requests.get(url)
            info.encoding = 'gbk'
            info_text = info.text
            soup = BeautifulSoup(info_text, 'html.parser')
            search_url = soup.find_all('p', class_='t1')
            for p in range(len(search_url)):
                a = search_url[p].a.get('href')
                f.write(a)
                f.write('\n')
                print('第{}条写完'.format(p + 1))
            print('第{}页写完'.format(i))


with open(r'C:\Users\20312\Desktop\qc1.txt', 'r') as f:
    a = f.read()
    print(a)


