import requests,re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

class Fuel:
    def __init__(self,url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    def One_page(self):
        fuel_info = requests.get(self.url,headers=self.headers).text
        soup = BeautifulSoup(fuel_info,'html.parser')
        page_info = soup.select('#leftTree > ul > li:nth-of-type(4) > ul > li:nth-of-type(1) > ul')[0]
        car_type = re.findall('<a class="dd " href="(.*?).html"><i class="icon-line"></i>(.*?)</a>',str(page_info))
        return car_type
    def Gain(self):
        url_list = self.One_page()
        for c,k in enumerate(url_list):
            print(k,789456)
            url ='https://price.pcauto.com.cn{}-p1.html'.format(k[0])
            print(url,789987)
            page_text = requests.get(url,headers=self.headers).text
            soup2 = BeautifulSoup(page_text,'html.parser')
            judge = soup2.find(class_='pcauto_page')
            print('正在爬取：'+str(c)+'页')
            if judge!=None:
                intt = judge.find_all('a')
                print(intt)
                for ii in intt[-2]:

                    print(ii,456852)

                for iii in range(1,int(ii)+1):
                    print(iii,000)
                    print(k,111)
                    print(k[0],222)
                    url2 = 'https://price.pcauto.com.cn{}-p{}.html'.format(k[0],iii)
                    print(url2)
                    info_page = requests.get(url2, self.headers,timeout=10).text
                    soup_info = BeautifulSoup(info_page, 'html.parser')
                    info_1 = soup_info.find(class_='listA').find_all(class_='info')
                    for cc,n in enumerate(info_1):
                        print('正在爬取：第' + str(cc) + '个'+'(多页)')
                        carname = n.find(class_='sname').text
                        officialprice = n.select('p:nth-of-type(2)')[0].text[4:]
                        carfuelc = n.select('p:nth-of-type(3)')[0].text[7:]
                        MIITfuelc = n.select('p:nth-of-type(5)')[0].text[6:]
                        rank = n.select('p:nth-of-type(6)')[0].text[3:]
                        displacement = n.select('p:nth-of-type(7)')[0].text[3:]
                        brand = n.select('p:nth-of-type(4)')[0].text[3:]
                        name_url = n.find(class_='sname').find('a').get('href')
                        car_url = requests.get('https://price.pcauto.com.cn{}'.format(name_url),headers=self.headers).text
                        soup3 = BeautifulSoup(car_url, 'html.parser')
                        gearbox_1 = soup3.select('ul > li:nth-of-type(2) > p:nth-of-type(1)')[0].find_all('a')
                        gearbox = []
                        for i in gearbox_1:
                            gearbox.append(i.text)
                        gearbox = gearbox[0]
                        cartype_1 = soup3.select('ul > li:nth-of-type(2) > p:nth-of-type(2)')[0].find_all('a')
                        cartype = []
                        for i in cartype_1:
                            cartype.append(i.text)
                        cartype = str(cartype).replace("']",'').replace("['",'').replace("'",'')
                        info_info = soup3.find(class_='strength')
                        ranking = info_info.find(class_='tip').text.replace('查看详情>>', '') 
                        carstrength = info_info.find(class_='score').text
                        configuration_s = info_info.find_all(class_='blue score')
                        m_info = []
                        for i in configuration_s:
                            m_info.append(i.text)
                        configuration = m_info[0]
                        major = m_info[1]
                        ownerevaluate = m_info[2]
                        price = m_info[3]

                        a = np.array([carname, officialprice, carfuelc, brand, MIITfuelc, rank, displacement, gearbox,str(cartype),ranking, carstrength, configuration, major, ownerevaluate, price])
                        df = pd.DataFrame(a).T
                        df.to_csv('pcauto.csv', mode='a', index=False, header=None, encoding='gbk')

        return 123
if __name__ == '__main__' :
    url = 'https://price.pcauto.com.cn/top/oil/s1-t1.html'
    a = Fuel(url)
    print(a.Gain())

