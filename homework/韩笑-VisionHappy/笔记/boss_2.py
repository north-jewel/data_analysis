import requests,re,csv
import pandas as pd
import numpy as np
#from proxies2 import Ip
class boss:
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    def __init__(self,
                 
                charset='utf-8',
                 url = 'https://www.zhipin.com/job_detail/?query=python&scity=101010100&industry=&position=',
                 
                ):
        self.url = url
        self.charset=charset
        self.html = self.response_html()
        self.Second_page = self.Second_page()
    def response_html(self):
        r = requests.get(self.url,headers=self.headers)
        
        r.encoding = self.charset
        
        return r.text
    def homepage_save(self):
        position_re='<div class="job-title">(.*?)</div>'
        salary_re='<span class="red">(.*?)</span>'        
        position = re.findall(position_re,self.html)
        salary=re.findall(salary_re,self.html)        
        data = {'position':position,'salary':salary}
        
        df = pd.DataFrame(data)
        return df
    
    def Second_page(self):
        
        details_re ='<a href="(.*?)" data-jid=".*?" data-itemid="\d*?" data-lid=".*?" data-jobid=".*?" data-index="\d*?" ka=".*?" target="_blank">'
        details=re.findall(details_re,self.html)
        for i in range(len(details)):
            url_1='https://www.zhipin.com/'+details[i]
            html_1 = requests.get(url_1).text
            city_required_edu_re='<p>城市：(.*?)<em class="vline"></em>经验：(.*?)<em class="vline"></em>学历：()</p>'
            company_name_re='<a ka="job-detail-company" href=".*?"  title=".*?" target="_blank">(.*?)</a>'          
            city_required_edu=re.findall(city_required_edu_re,html_1)
            company_name = re.findall(company_name_re,html_1)
            data_1 = {'company_city':city_required_edu[0][0],'company_required':city_required_edu[0][1],'edu_required':city_required_edu[0][2]}
            df2 = pd.DataFrame(data_1)
            print(df2)
            print(city_required_edu)
            return city_required_edu
        
boss()
