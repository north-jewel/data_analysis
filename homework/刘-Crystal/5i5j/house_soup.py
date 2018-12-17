from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
class House:
    chrome_options = webdriver.ChromeOptions ()
    chrome_options.add_argument ('--headless')
    driver = webdriver.Chrome (options=chrome_options)

    def __init__(self,
                 url='https://bj.5i5j.com/zufang/42129766.html'
                 ):
        self.url = url
        self.soup = self.get_html()
        self.circle_info()
        self.house_info()

    def get_html(self):
        self.driver.get (self.url)
        message = self.driver.page_source
        soup = BeautifulSoup (message, 'html.parser')
        return soup

    def key_word(self):
        try:
            house_keyword = self.soup.select ('h1.house-tit')[0].text
        except IndexError:
            house_keyword = np.nan
        return house_keyword

    def circle_info(self):
        try:
            all_info = self.soup.select('div.jlquannei > p.jlinfo')
        except IndexError:
            all_info = np.nan
        return all_info

    def rent_house(self):
        try:
            rent = self.circle_info()[0].text
        except IndexError:
            rent = np.nan
        return rent

    def house_type(self):
        try:
            house_type_1 = self.circle_info()[1].text
        except IndexError:
            house_type_1
        return house_type_1

    def area_house(self):
        try:
            area = self.circle_info()[2].text
        except IndexError:
            area = np.nan
        return area

    def payment_house(self):
        try:
            payment = self.circle_info()[3].text
        except IndexError:
            payment = np.nan
        return payment

    def house_info(self):
        try:
            house_info_1 = self.soup.select('div.zushous > ul > li')
        except IndexError:
            house_info_1 = np.nan
        return house_info_1

    def district_house(self):
        try:
            
            district = self.house_info()[0].text.replace ('小区：', '')
        except IndexError:
            district = np.nan
        return district

    def floor_house(self):
        try:
            floor = self.house_info()[1].text.replace('楼层：', '')
        except IndexError:
            floor = n.nan
        return floor

    def orientation_house(self):
        try:
            orientation = self.house_info()[2].text.replace('朝向：', '')
        except IndexError:
            orientation = np.nan
        return orientation

    def decoration_house(self):
        try:
            decoration = self.house_info()[3].text.replace('装修：', '')
        except IndexError:
            decoration = np.nan
        return decoration

    def tower_type_house(self):
        try:
            tower_type = self.house_info()[4].text.replace ('楼型：', '')
        except IndexError:
            tower_type = np.nan
        return tower_type

    def heating_house(self):
        try:
            heating = self.house_info()[5].text.replace ('供暖：', '')
        except IndexError:
            heating = np.nan
        return heating

    def rent_way_house(self):
        try:
            rent_way = self.house_info()[6].text.replace ('出租方式：', '')
        except IndexError:
            rent_way = np.nan
        return rent_way

    def look_time_house(self):
        try:
            look_time = self.house_info()[7].text.replace ('看房时间：', '')
        except IndexError:
            look_time = np.nan
        return look_time

    def trading_area_house(self):
        try:
            
            trading_area = self.house_info()[8].text.replace ('商圈：', '')
        except IndexError:
            trading_area = np.nan
        return trading_area

    def metor_house(self):
        try:
            metor = self.house_info()[9].text.replace ('地铁：', '')
        except IndexError:
            metor = np.nan
        return metor

    def house_fun(self):
        try:
            house_app = self.soup.select('ul.fysty > li')
            equipment = []
            for i in house_app:
                equipment.append(i.text)
        except IndexError:
            equipment = np.nan

        return equipment




