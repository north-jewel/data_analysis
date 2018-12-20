import requests,re,os,glob
from bs4 import BeautifulSoup
from selenium import webdriver
import time


inut  = input('请输入id')
url = 'https://music.163.com/artist?id={}'.format(inut)#歌手id

drive = webdriver.Chrome()
drive.get(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
info = requests.get(url,headers=headers)
r = BeautifulSoup(info.content,'html.parser')

result = r.find('ul',{'class','f-hide'}).find_all('a')
for music in result:
    music_id = music.get('href')
    idd = music_id.replace('/song?id=','')
    print(music.text)
    uu = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(idd)
    cc= requests.get(uu,headers=headers)
    with open('{}.mp3'.format(music.text), 'wb')as f:
       f.write(cc.content)
