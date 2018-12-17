from selenium import webdriver
from bs4 import BeautifulSoup
from house_soup import House
import pandas as pd
import numpy as np
import os
class MeHome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    def __init__(self,
                 url='https://bj.5i5j.com/zufang/n2',

                 ):
        self.url = url

        self.get_url = self.get_url()

    def get_url(self):
        self.driver.get(self.url)
        message = self.driver.page_source
        soup = BeautifulSoup(message, 'html.parser')
        every_url = soup.select('div.listCon > h3.listTit > a')
        every_url_list = []
        for every_url_1 in every_url:
            every_url_list.append(every_url_1.get('href'))
        return every_url_list

    def get_info(self):
        house_info = {}
        for house_url in self.get_url:
            a = []
            house_url ='https://bj.5i5j.com{}'.format(house_url)

            h_k = House(house_url).key_word()
            rent = House(house_url).rent_house()
            house_type_h = House(house_url).house_type()
            area = House(house_url).area_house()
            payment = House(house_url).payment_house()
            district = House(house_url).district_house()
            floor = House(house_url).floor_house()
            orientation = House(house_url).orientation_house()
            decoration = House(house_url).district_house()
            tower_type = House(house_url).tower_type_house()
            heating = House(house_url).heating_house()
            rent_way = House(house_url).rent_way_house()
            look_time = House(house_url).look_time_house()
            trading_area = House(house_url).trading_area_house()
            metor = House(house_url).metor_house()
            equipment = House(house_url).house_fun()
            a.append(equipment)
            print(a)
            house_info= {'house_url':house_url,
                        'houskeyword': h_k,
                        'rent': rent,
                        'housetype': house_type_h,
                        'area':area,
                        'payment':payment,
                        'district':district,
                        'tage' : floor,
                        'orientation':orientation,
                        'decoration':decoration,
                        'towertype':tower_type,
                        'heating':heating,
                        'rentway':rent_way,
                        'looktime':look_time,
                        'tradingarea':trading_area,
                        'metor	':metor,
                        'housing_facilities':a}
            df = pd.DataFrame(house_info)
            path = os.getcwd()+'\\5i5j.csv'
            df.to_csv(path,mode='a',header = False,encoding = 'utf-8',index = None)




for i in range(1,11):
    m = MeHome(url = 'https://bj.5i5j.com/zufang/n{}'.format(i))
    m.get_info()
