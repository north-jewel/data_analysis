import re,requests,json
import pandas as pd
import numpy as np

class ZhaoPin:
    def __init__(self,headers,i=1,out_url_i = 530):
        self.header = headers
        self.outer_url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId={}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&at=cb61f0195d5c4ebb8f41a288ae4f73f6&rt=cb54cccaa3284157b54994180426de07&_v=0.84894372&userCode=715503136&x-zp-page-request-id=d0446ce1e4ca4f49b0837535845f1c28-1543566149032-12188'.format(60*i,out_url_i)
    def Outer_url(self):
        outer_info = requests.get(self.outer_url,headers=self.header)
        json_response = outer_info.content.decode()
        dict_json = json.loads(json_response)
        for i in range(len(dict_json['data']['results'])):
        #print(len(dict_json['data']['results']))
        #for i in range(2):
            corporation_url = dict_json['data']['results'][i]['positionURL']#公司url
            interior_info = requests.get(corporation_url,headers=self.header).text

            city = dict_json['data']['results'][i]['city']['items'][0]['name']
            skill_type = dict_json['data']['results'][i]['jobType']['items'][1]['name']
            company_name = dict_json['data']['results'][i]['company']['name']
            company_size = dict_json['data']['results'][i]['company']['size']['name']
            company_type = dict_json['data']['results'][i]['company']['type']['name']
            edu_required = dict_json['data']['results'][i]['eduLevel']['name']
            experience_required = dict_json['data']['results'][i]['workingExp']['name']
            company_welfar = dict_json['data']['results'][i]['welfare']
            company_welfar = str(company_welfar).replace("'",'').replace(',','')
            updateDate = dict_json['data']['results'][i]['updateDate']
            endDate = dict_json['data']['results'][i]['endDate']
            salary = dict_json['data']['results'][i]['salary']
            job_required = dict_json['data']['results'][i]['emplType']
            a = np.array([city,skill_type,company_name,company_size,company_type,edu_required,experience_required,company_welfar,updateDate,endDate,salary,job_required])
            df = pd.DataFrame(a).T
            print(a)
            df.to_csv('zhaopin.csv',mode='a',index=False,header=None,encoding='gbk')


        return 'over'

if __name__ == '__main__':
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    #out_url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&at=cb61f0195d5c4ebb8f41a288ae4f73f6&rt=cb54cccaa3284157b54994180426de07&_v=0.84894372&userCode=715503136&x-zp-page-request-id=d0446ce1e4ca4f49b0837535845f1c28-1543566149032-12188'
    for i in range(1,3):
        ZhaoPin(headers,i=i).Outer_url()
