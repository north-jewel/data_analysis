"""

@author:tts

@file: Pacific_car.py

@time: 2018/12/15

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

class reptile_car:
    url1 = 'https://price.pcauto.com.cn/top/oil/s1-t2.html'
    def __init__(self):
        self.page = self.zong_page()#获取到总页数

    def zong_page(self):
        url_obj = requests.get(self.url1)
        url_obj.encoding = 'gbk'
        url_text = url_obj.text
        soup = BeautifulSoup(url_text,'html.parser')
        pages = soup.find('ul',class_="").find_all('a')
        car_type_url = []
        # car_url = {}
        for i in pages:
            # car_url[i.text.strip()] = 'https://price.pcauto.com.cn'+i.get('href')
            car_type_url.append('https://price.pcauto.com.cn'+i.get('href'))

        return car_type_url

    def car_xinxi(self,url):
        car_obj = requests.get(url)
        car_obj.encoding = 'gbk'
        car_text = car_obj.text
        soup = BeautifulSoup(car_text, 'html.parser')
        panduan = soup.find('div', class_="pcauto_page")
        if panduan == None:#只有一页
            #里面有链接和所有车的名字
            sname = soup.find_all('p',class_='sname')
            #一个车的6个信息全在里面
            col = soup.find_all('p', class_='col')
            carname =[]#车名
            officialprice =[] #官方价格
            carfuelc =[] #车主平均油耗
            brand =[] #品牌
            MIITfuelc =[] #工信部油耗
            rank =[] #车型
            displacement=[] #排量
            juti_car_url =[]
            gearbox =[] #变速箱
            cartype =[] #车身类型
            ranking =[] #排名
            carstrength =[] #车实力
            configuration =[] #配置水平:
            major =[] #专业测评
            ownerevaluate =[] #车主评价
            price =[] #price
            for i in sname:
                carname.append(i.find('a').text.strip())
                juti_car_url.append('https://price.pcauto.com.cn'+i.find('a').get('href'))
            one_car = 0

            for x in col:
                one_car+=1
                if one_car ==1:
                    officialprice.append(x.find('em').text.strip())
                if one_car ==2:
                    carfuelc.append(x.find('em').text.strip())
                if one_car ==3:
                    brand.append(x.text.strip().replace('品牌：',''))
                if one_car ==4:
                    MIITfuelc.append(x.text.strip().replace('工信部油耗：',''))
                if one_car ==5:
                    rank.append(x.text.strip().replace('级别：',''))
                if one_car ==6:
                    displacement.append(x.text.strip().replace('排量：',''))
                    one_car = 0

            for y in juti_car_url:
                print(y)
                car_xinxi = self.car_juti(y)

                gearbox.append(car_xinxi[0])
                cartype.append(car_xinxi[1])
                ranking.append(car_xinxi[2])
                carstrength.append(car_xinxi[3])
                configuration.append(car_xinxi[4])
                major.append(car_xinxi[5])
                ownerevaluate.append(car_xinxi[6])
                price.append(car_xinxi[7])
            zong_car={
                '车名':carname,
                '官方价':officialprice,
                '车主平均油耗':carfuelc,
                '品牌':brand,
                '工信部油耗':MIITfuelc,
                '级别':rank,
                '排量':displacement,
                '变速箱':gearbox,
                '车身类型':cartype,
                '排名':ranking,
                '车实力':carstrength,
                '配置水平':configuration,
                '专业测评':major,
                '车主评价':ownerevaluate,
                '价格':price
            }
            df_car = pd.DataFrame(zong_car)
            try:
                pd.read_csv(r'taipingyang.csv')
            except:
                df_car.to_csv(r'taipingyang.csv',header=True,mode='a', encoding='utf_8_sig',index = False)
            else:
                df_car.to_csv(r'taipingyang.csv',header=False,mode='a', encoding='utf_8_sig',index = False)
        else:#有很多页
            car_type_pages = panduan.find_all('a')[-2].text
            for q in range(1,int(car_type_pages)+1):
                car_type_url = url.replace('.html','')
                new_car_type_url = car_type_url+'-p'+str(q)+'.html'
                new_car_type_obj = requests.get(new_car_type_url)
                new_car_type_obj.encoding = 'gbk'
                new_car_type_text = new_car_type_obj.text
                soup=BeautifulSoup(new_car_type_text,'html.parser')
                sname = soup.find_all('p', class_='sname')
                # 一个车的6个信息全在里面
                col = soup.find_all('p', class_='col')
                carname = []  # 车名
                officialprice = []  # 官方价格
                carfuelc = []  # 车主平均油耗
                brand = []  # 品牌
                MIITfuelc = []  # 工信部油耗
                rank = []  # 车型
                displacement = []  # 排量
                juti_car_url = []
                gearbox = []  # 变速箱
                cartype = []  # 车身类型
                ranking = []  # 排名
                carstrength = []  # 车实力
                configuration = []  # 配置水平:
                major = []  # 专业测评
                ownerevaluate = []  # 车主评价
                price = []  # price
                for i in sname:
                    carname.append(i.find('a').text.strip())
                    juti_car_url.append('https://price.pcauto.com.cn' + i.find('a').get('href'))
                one_car = 0
                for x in col:
                    one_car += 1
                    if one_car == 1:
                        officialprice.append(x.find('em').text.strip())
                    if one_car == 2:
                        carfuelc.append(x.find('em').text.strip())
                    if one_car == 3:
                        brand.append(x.text.strip().replace('品牌：', ''))
                    if one_car == 4:
                        MIITfuelc.append(x.text.strip().replace('工信部油耗：', ''))
                    if one_car == 5:
                        rank.append(x.text.strip().replace('级别：', ''))
                    if one_car == 6:
                        displacement.append(x.text.strip().replace('排量：', ''))
                        one_car = 0
                for y in juti_car_url:
                    print(y)
                    car_xinxi = self.car_juti(y)
                    gearbox.append(car_xinxi[0])
                    cartype.append(car_xinxi[1])
                    ranking.append(car_xinxi[2])
                    carstrength.append(car_xinxi[3])
                    configuration.append(car_xinxi[4])
                    major.append(car_xinxi[5])
                    ownerevaluate.append(car_xinxi[6])
                    price.append(car_xinxi[7])
                zong_car = {
                    '车名': carname,
                    '官方价': officialprice,
                    '车主平均油耗': carfuelc,
                    '品牌': brand,
                    '工信部油耗': MIITfuelc,
                    '级别': rank,
                    '排量': displacement,
                    '变速箱': gearbox,
                    '车身类型': cartype,
                    '排名': ranking,
                    '车实力': carstrength,
                    '配置水平': configuration,
                    '专业测评': major,
                    '车主评价': ownerevaluate,
                    '价格': price
                }
                df_car = pd.DataFrame(zong_car)
                try:
                    pd.read_csv(r'taipingyang.csv')
                except:
                    df_car.to_csv(r'taipingyang.csv', header=True, mode='a', encoding='utf_8_sig', index=False)
                else:
                    df_car.to_csv(r'taipingyang.csv', header=False, mode='a', encoding='utf_8_sig', index=False)





    def car_juti(self,urls):
        juti_url =urls
        juti_url_obj = requests.get(juti_url)
        juti_url_obj.encoding='gbk'
        juti_url_text = juti_url_obj.text
        soup = BeautifulSoup(juti_url_text,'html.parser')
        gearbox = \
        soup.select('#detail > div.box-b > div.infor > div.price > ul > li:nth-of-type(2) > p:nth-of-type(1) > em')[0].text
        # print(juti_url)
        # print(gearbox)

        cartypes = soup.select('#detail > div.box-b > div.infor > div.price > ul > li:nth-of-type(2) > p:nth-of-type(2) > em > a:nth-of-type(1)')
        cartype = cartypes[0].text.strip()
        ranking = soup.select('#strengthProcess > p')[0].text.strip().replace('查看详情>>', '')
        carstrength = soup.find('p',class_='score').text.strip()
        configuration = soup.select('#strengthProcess > div.processBarWrap > div:nth-of-type(1) > div > p')[0].text.strip()
        major = soup.select('#strengthProcess > div.processBarWrap > div:nth-of-type(2) > div > p')[0].text.strip()
        ownerevaluate = soup.select('#strengthProcess > div.processBarWrap > div:nth-of-type(3) > div > p')[0].text.strip()
        price = soup.select('#strengthProcess > div.processBarWrap > div:nth-of-type(4) > div > p')[0].text.strip()
        return  gearbox,cartype,ranking,carstrength,configuration,major,ownerevaluate,price


if __name__ == "__main__":
    r_c = reptile_car()
    car_list_url = r_c.zong_page()
    for c in car_list_url:
        r_c.car_xinxi(c)

