from bs4 import BeautifulSoup
import requests

class Pcauto:

    def __init__(self, url='https://price.pcauto.com.cn/top/oil/s1-t2.html', charset='gb2312',):
        self.url = url
        self.charset = charset
        self.pto_text = self.pcauto_html()
        self.soup = BeautifulSoup(self.pto_text, 'html.parser')


    def pcauto_html(self):
        res = requests.get(self.url)
        res.encoding = self.charset
        return res.text


    def car_type(self):

        car_type = self.soup.find('ul', class_='').find_all('a', class_='dd')

        return car_type


    def page(self):

        page = self.soup.select('div.pcauto_page > a')

        return page


    def car_info(self):

        car_info = self.soup.find_all('div', class_='info')
        car_dict_list = []
        for info in car_info:
            car_dict_list.append({'carname': info.find('p', class_='sname').text.strip(),
                                  'officialprice': info.find_all('p', class_='col')[0].text.split('：')[-1].strip(),
                                  'carfuelc': info.find_all('p', class_='col')[1].text.split('：')[-1].strip(),
                                  'brand': info.find_all('p', class_='col')[2].text.split('：')[-1].strip(),
                                  'MIITfuelc': info.find_all('p', class_='col')[3].text.split('：')[-1].strip(),
                                  'rank': info.find_all('p', class_='col')[4].text.split('：')[-1].strip(),
                                  'displacement': info.find_all('p', class_='col')[5].text.split('：')[-1].strip(),
                                  'url': 'https://price.pcauto.com.cn' + info.select_one('p.sname > a').get('href'), })

        return car_dict_list


    def car_info1(self):

        # 变速箱info
        gearbox = self.soup.find('ul', class_='des').find_all('p')[2].find('a').text.strip()
        # 车身类型info
        cartype = self.soup.find('ul', class_='des').find_all('p')[3].find('a').text.strip()
        # 排名info
        ranking = self.soup.select_one('div#strengthProcess > p').text.replace('查看详情>>', '').strip()
        # 车实力info
        carstrength = self.soup.select('div.processBar-txt  > p')[0].text.strip()
        # 配置水平info
        configuration = self.soup.select('div.processBar-txt  > p')[1].text.strip()
        # 专业测评info
        major = self.soup.select('div.processBar-txt  > p')[2].text.strip()
        # 车主评价info
        ownerevaluate = self.soup.select('div.processBar-txt  > p')[3].text.strip()
        # 价格info
        price = self.soup.select('div.processBar-txt  > p')[4].text.strip()

        car_info_dict = {'gearbox': gearbox,
                         'cartype': cartype,
                         'ranking': ranking,
                         'carstrength': carstrength,
                         'configuration': configuration,
                         'major': major,
                         'ownerevaluate': ownerevaluate,
                         'price': price, }
        #print(car_info_dict)
        return car_info_dict






if __name__ == '__main__':
    pto_obj = Pcauto(url='https://price.pcauto.com.cn/top/oil/s1-t3.html')
    pto_obj.car_info()

# try:
#     page = int(self.soup.select('div.pcauto_page > a')[-2].text.strip())
# except IndexError:
#     page = 1
# else:
#     page = page


