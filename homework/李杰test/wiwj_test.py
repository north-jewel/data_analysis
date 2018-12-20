import requests,re
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time


class WIWJ:
    def __init__(self,sum):
        self.list_ua = ['Mozilla/5.0 (Linux; Android 7.1.1; MI MAX 2 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043520 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080',
                        'Mozilla/5.0 (Linux; Android 7.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 YaBrowser/17.9.0.523.00 Mobile Safari/537.36',
                        'Mozilla/5.0 (Linux; Android 6.0.1; SM-A9000 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile UCBrowser/6.2 TBS/043613 Safari/537.36',
                        'Mozilla/5.0 (Linux; Android 6.0.1; MI NOTE LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043805 Mobile Safari/537.36 MicroMessenger/6.6.1200(0x26060031) NetType/4G Language/zh_CN',
                        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 AliApp(DingTalk/4.2.6) com.laiwang.DingTalk/3058829 Channel/201200 language/zh-Hans',
                        'Mozilla/5.0 (Linux; Android 7.0; MI 5s Plus Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.2.1240(0x26060235) NetType/4G Language/zh_CN',
                        'Mozilla/5.0 (Linux; Android 7.1.1; 4A Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 V1_AND_SQ_7.5.0_794_YYB_D QQ/7.5.0.3430 NetType/WIFI WebP/0.3.0 Pixel/720',
                        'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3',
                        'Mozilla/5.0 (Linux; Android 6.0.1; SM-A5108 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043602 Safari/537.36 V1_AND_SQ_7.1.8_718_YYB_D QQ/7.1.8.3240 NetType/WIFI WebP/0.3.0 Pixel/1080',
                        'Mozilla/5.0 (Linux; Android 7.0; Mi-4c Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080',
                        'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/WIFI WebP/0.3.0 Pixel/1080',
                        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) CriOS/62.0.3202.70 Mobile/14E304 Safari/602',
                        'Mozilla/5.0 (Linux; Android 7.0; SM-G9308 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043610 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN',
                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4467.400 QQBrowser/10.0.424.400',
                        'Mozilla/5.0 (Linux; Android 8.0; TA-1000 Build/OPR1.170623.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043908 Mobile Safari/537.36 V1_AND_SQ_7.1.0_0_TIM_D TIM2.0/2.0.0.1696 QQ/6.5.5 NetType/WIFI WebP/0.3.0 Pixel/1080 IMEI/null',
                        'Mozilla/5.0 (iPhone; CPU iPhone OS 10.3 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3 QHBrowser/271 QihooBrowser/4.0.1',
                        'Mozilla/5.0 (Linux; Android 7.1.1; SM-N9500 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 V1_AND_SQ_7.5.0_794_YYB_D QQ/7.5.0.3430 NetType/4G WebP/0.3.0 Pixel/1080',
                        'Mozilla/5.0 (Linux; Android 7.0; Mi-4c Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043813 Mobile Safari/537.36 V1_AND_SQ_7.3.2_762_YYB_D QQ/7.3.2.3350 NetType/WIFI WebP/0.3.0 Pixel/1080',
                        'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043806 Mobile Safari/537.36 V1_AND_SQ_7.3.2_762_YYB_D QQ/7.3.2.3350 NetType/WIFI WebP/0.3.0 Pixel/1080',
                        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
                        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
                        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
                        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
                        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
                        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
                        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
                        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
                        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
                        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
                        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
                        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201',
                        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                        ]

        self.sum =sum+1
        self.headers = { 'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 '}
    def Page_url(self):
        page_url_list = []
        for i in range(1,self.sum):
            page_url ='https://bj.5i5j.com/zufang/n{}/'.format(i)
            page_url_list.append(page_url)
        return page_url_list
    def Ua(self):
        UA = dict({'User-Agent': np.random.choice(self.list_ua, 1)[0]})
        return UA
    def Cycl(self,a,b):
        global S_S
        S_S= requests.Session()
        single_info = S_S.get(a,headers=self.Ua()).text
        fake_url_F = re.findall('<p><b>URL : </b><span>(.*?)</span></p>',single_info)
        #print(fake_url_F,000)
        if fake_url_F == []:
            fake_url = re.findall("<script>window.location.href='(.*?)';</script>", single_info)
        else:
            fake_info = S_S.get(fake_url_F[0],headers=self.Ua()).text
            fake_url = re.findall("<script>window.location.href='(.*?)';</script>",fake_info)
            if fake_url == []:
                fake_urll = a
                ckk = S_S.get(a, headers=self.Ua()).text
                print(ckk)
                fake_url = re.findall('<p><b>URL : </b><span>(.*?)</span></p>', ckk)
                if fake_url==[]:
                    fake_url = re.findall("<script>window.location.href='(.*?)';</script>",ckk)
                print(fake_url,5555555)
        #print(a,1111111,fake_url_F,222222,fake_url)
        return fake_url
    def Single(self):
        url =self.Page_url()
        for i,ii in enumerate(url):

                print('正在爬取第：' + str(i + 1) + '页')
                real_url = self.Cycl(ii,i)[0]
                print(real_url,44444444444)
                real_info = S_S.get(real_url, headers=self.Ua()).text
                soup = BeautifulSoup(real_info, 'html.parser')
                house_name_list = soup.find(class_='pList')
                if house_name_list == []:
                    print(real_url,333333333)
                    continue
                house_name_li = house_name_list.find_all(class_='listTit')

                for ck,dk in enumerate(house_name_li):
                    print('正在抓取第：'+str(ck+1)+'个')
                    house_url = 'https://bj.5i5j.com'+dk.find('a').get('href')
                    houskeyword = dk.find('a').text
                    real_url_2 = self.Cycl(house_url,ck)[0]
                    real_info_2 = S_S.get(real_url_2,headers=self.Ua()).text
                    soup2 = BeautifulSoup(real_info_2,'html.parser')
                    renting_info = soup2.find_all(class_='jlinfo')
                    try:
                        rent = renting_info[0].text                     #租金
                        housetype = renting_info[1].text                #户型
                        area =renting_info[2].text                      #面积
                        payment = renting_info[3].text                  #支付方式
                        if len(list(renting_info)) <5:
                            record_list = [np.nan,np.nan,np.nan]
                        else:
                            record_list = [renting_info[4].text,renting_info[5].text,renting_info[6].text]      #带看记录
                        record_recently = record_list[0]
                        record_week = record_list[1]
                        record_month = record_list[2]
                        building_info = soup2.find(class_='zushous')
                        detail_info=re.findall('</span>(.*?)</li>',str(building_info))
                        district =re.findall('[\u4E00-\u9FA5]+',str(detail_info[0]))[0]#小区

                        tage =detail_info[1]            #楼层
                        orientation = detail_info[2]    #朝向
                        decoration = detail_info[3]     #装修
                        towertype = detail_info[4]      #楼型
                        heating = detail_info[5]        #供暖
                        rentway = detail_info[6]        #整租
                        looktime = detail_info[7]       #看房时间
                        tradingarea = detail_info[8]    #商圈
                        metor_X = building_info.find(class_='traffic')
                        if metor_X == None:
                            metor=np.nan
                        if metor_X !=None:
                            metor =metor_X.text.replace('地铁：','')
                        housingfacilities_info = soup2.find(class_='tag-now clear').find_all('li')
                        housingfacilities_list = []
                        for ic in housingfacilities_info:
                            housingfacilities_list.append(ic.text)        #房源配套设施
                        developers_l = soup2.find(class_ = 'infomain fl').select('ul > li:nth-of-type(2)')[0].text
                        developers = np.nan
                        if '开发商' in developers_l:
                            developers=str(developers_l).replace('开发商','')         #开发商
                        a = np.array([houskeyword,rent,housetype,area,payment,district,tage,orientation,decoration,towertype,heating,rentway,looktime,tradingarea,metor,str(housingfacilities_list),record_recently,record_week,record_month,developers])
                        print(a)
                        df = pd.DataFrame(a).T
                        df.to_csv('woaiwojia_test.csv', mode='a', index=False, header=None, encoding='gbk')

                    except:
                        print(renting_info)
                    else:
                        print(111111111)


if __name__ == '__main__':
    a = WIWJ(10)
    print(a.Single())