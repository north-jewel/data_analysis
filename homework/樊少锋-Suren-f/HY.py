import requests
import re
import numpy as np
import pandas as pd
import urllib
from bs4 import BeautifulSoup



#url = ''

def get_url():

    url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2793&tagAll=0'
    headers = {

        'referer':'https://www.huya.com/g/2793',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/69.0.3497.81 Safari/537.36',
    }
    info = requests.get(url,headers)
    info.encoding = 'utf-8'
    if info.status_code == 200:
        info_json = info.json()
        return info_json['data']['datas'][0]
print(get_url())
def get_info():
    live_info = []
    for i in get_url():
        nick = i['nick']
        live_info.append(nick)
        #直播名字
        introduction = i['introduction']
        live_info.append(introduction)
        #直播标题
        bluRayMBitRate = i['bluRayMBitRate']
        live_info.append(bluRayMBitRate)
        #视频清晰度
        profileRoom = i['profileRoom']
        live_info.append(profileRoom)
        #房间号

    live_data = []
    x = 0
    for i in range(len(live_info) // 4):
        live_data.append([z for z in live_info[x:x + 4]])
        x = x + 4

    return live_data
def write_csv():
    data = get_info()
    df = pd.DataFrame(data,columns=['直播名字','直播标题','视屏清晰度','房间号'])
    print(df)
    df.to_csv('3.csv', index=False, encoding='utf-8-sig')
    return '完成'



print(write_csv())
