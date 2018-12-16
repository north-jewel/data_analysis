import pandas as pd
import requests
import re


class TaiPingYang:
    def __init__(self,
                 url='https://price.pcauto.com.cn/top/oil/s1-t{}.html',
                 charset='gbk',
                 headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
                 ):
        self.url = url
        self.charset = charset
        self.headers = headers
        self.get_rank = self.get_rank()
        self.get_html = self.get_html()
        self.get_info = self.get_info()

    def get_rank(self):
        '''
        获取油耗排行榜的所有类型链接
        :return:油耗排行榜的列表
        '''
        rank_url = []
        for i in range(2,21):
            if i == 13:
                pass
            else:
                rank_url.append(self.url.format(i))
        # print(rank_url)
        return rank_url

    def get_html(self):
        '''
        获取太平洋汽车网小型车油耗排行榜
        :return:html的所有内容
        '''
        url_str = ''
        for i in self.get_rank:
            res = requests.get(i,headers=self.headers)
            res.encoding = self.charset
            url_str += res.text
        # print(url_str)
        return url_str

    def get_url(self):
        '''
        获取所有的跳转链接
        :return: 返回所有的跳转链接
        '''
        carurl = '<p class="sname"><a href="(.*?)"'
        car_wear_url = []
        car_url = re.findall(carurl,self.get_html)
        for i in car_url:
            url_car = 'https://price.pcauto.com.cn{}'.format(i)
            car_wear_url.append(url_car)
        #print(car_wear_url)
        return car_wear_url

    def get_info(self):
        '''获取小型车主页信息'''
        car_name = '<p class="sname"><a href=".*?" target="_blank">(.*?)</a></p>' #车名
        official_price = '<p class="col col1">官方价：<em class="red">(.*?)</em></p>' #官方价格
        car_fuelc = '<p class="col">车主平均油耗：<em class="red">(.*?)</em></p>' #车主平均油耗
        car_brand = '<p class="col col1">品牌：(.*?)</p>' #汽车品牌
        car_MIITfuelc = '<p class="col">工信部油耗：(.*?)</p>'  #工信部油耗
        car_rank = '<p class="col col1">级别：(.*?)</p>' #级别
        car_displacement = '<p class="col">排量：<a href=".*?" target="_blank" title=".*?">(.*?)</a>' #汽车排量

        carname = re.findall(car_name,self.get_html)
        officialprice = re.findall(official_price, self.get_html)
        carfuelc = re.findall(car_fuelc,self.get_html)
        brand = re.findall(car_brand,self.get_html)
        MIITfuelc = re.findall(car_MIITfuelc,self.get_html)
        rank = re.findall(car_rank, self.get_html)
        displacement = re.findall(car_displacement,self.get_html)
        # print(carname)
        # print(officialprice)
        # print(carfuelc)
        # print(brand)
        # print(MIITfuelc)
        # print(rank)
        # print(displacement)
        return [carname,officialprice,carfuelc,brand,MIITfuelc,rank,displacement]

    def save_home(self):
        '''用DataFrame保存成csv'''
        df = pd.DataFrame(columns=['carname','officialprice','carfuelc','brand','MIITfuelc','rank','displacement'])
        df1 = pd.DataFrame(data = self.get_info).T
        df1.columns = ['carname','officialprice','carfuelc','brand','MIITfuelc','rank','displacement']
        df2 = pd.concat([df,df1])
        df2.to_csv('主页信息.csv',index=None,encoding='utf-8-sig')
        print('保存成功!')
if __name__ == '__main__':

    car = TaiPingYang()
    car.save_home()
