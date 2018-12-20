import requests
import re
import json
import pandas as pd
import numpy as np


class Recruit:


    def __init__(self,header,i = 1,city_id = 530):

        self.cy_url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId={}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&at=a275bca65e8b4136b55c6bb223c1aea1&rt=981eb27123d242d6be6093d2bb044c0d&_v=0.98147050&userCode=1019607413&x-zp-page-request-id=a3e3427a59934048b74c8c6150c4f810-1543748402994-610686'.format(i*60,city_id)
        self.headers = header

    def Cy_url(self):
        out_info = requests.get(self.cy_url).json()

        for i in range(len(out_info['data']['results'])):
            city = out_info['data']['results'][i]['city']['items'][0]['name']
            skill_type = out_info['data']['results'][i]['jobType']['items'][0]['name']
            companys_name = out_info['data']['results'][i]['company']['name']
            companys_size = out_info['data']['results'][i]['company']['size']['name']
            companys_type = out_info['data']['results'][i]['company']['type']['name']
            edu_required = out_info['data']['results'][i]['eduLevel']['name']
            experience_required = out_info['data']['results'][i]['workingExp']['name']
            companys_salary = out_info['data']['results'][i]['salary']
            companys_names = out_info['data']['results'][i]['jobName']
            companys_welfare = out_info['data']['results'][i]['welfare']
            companys_welfare = str(companys_welfare).replace("'",'').replace(',','')
            a = np.array([city,skill_type,companys_name,companys_size,companys_type,edu_required,experience_required,companys_salary,companys_names,companys_welfare])
            df = pd.DataFrame(a).T
            df.to_csv(r'C:\Users\Shilin\Desktop\emm.csv',encoding='gbk',header = None,index = False,mode = 'a')



if __name__ == '__main__':
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    for i in range(1, 5):
        Recruit(header,i = i).Cy_url()
