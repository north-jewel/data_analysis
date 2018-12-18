from pcauto import *
import numpy as np
import pandas as pd


class SpiderPcauto:
    def __init__(self, url='https://price.pcauto.com.cn/top/oil/s1-t3.html'):
        self.url = url
        self.url_dict = self.car_type_info()
        #self.car_info_list = self.spider_info()


    def car_type_info(self):

        pto_obj = Pcauto(url=self.url)
        bs4_list = pto_obj.car_type()

        url_dict = {}

        for x in bs4_list:

            url_dict[x.text.strip()] = 'https://price.pcauto.com.cn/' + x.get('href')

        return url_dict



    def spider_info(self):


        for key in self.url_dict:
            pto_obj = Pcauto(url=self.url_dict[key])
            page_list = pto_obj.page()
            url_dict = {}
            if page_list != []:
                url_list = []
                max_page = int(page_list[-2].text.strip())
                for page in range(1, max_page + 1):
                    url_list.append(self.url_dict[key].replace('.html', '') + '-p{}.html'.format(page))
                url_dict[key] = url_list
            else:
                url_dict[key] = [self.url_dict[key]]
            y = 0
            for url in url_dict[key]:
                pto_obj = Pcauto(url=url)
                info_dict_list = pto_obj.car_info()

                y += 1
                n = 0
                for info_dict in info_dict_list:
                    pto_obj1 = Pcauto(url=info_dict['url'])
                    info_dict1 = pto_obj1.car_info1()
                    info_dict.update(info_dict1)
                    n += 1
                    print('正在保存{}的第{}页第{}条数据·····'.format(key, y, n))
                    df = pd.DataFrame.from_dict(info_dict, orient='index').T
                    try:
                        pd.read_csv(r'C:\Users\yk\Desktop\pcauto_info.csv')
                    except FileNotFoundError:
                        df.to_csv(r'C:\Users\yk\Desktop\pcauto_info.csv', index=False, encoding='utf_8_sig')
                    else:
                        df.to_csv(r'C:\Users\yk\Desktop\pcauto_info.csv', index=False, header=None, mode='a', encoding='utf_8_sig')







if __name__ == '__main__':
    a = SpiderPcauto(url='https://price.pcauto.com.cn/top/oil/s1-t2.html')
    b = a.spider_info()

