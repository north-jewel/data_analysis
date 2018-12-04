import requests
import re

class QianCheng:
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    def __init__(self,url):
        self.url=url
        self.header=self.header
        self.content = self.content()
        self.links=self.links()
    def content(self):
        html=requests.get(self.url,headers=self.header)
        html.encoding='gbk'
        return html.text
    def links(self):
        reg = re.compile(r'class="t1 ">.*? <a target="_blank" title=".*?" href="(.*?)".*? <span class="t2">', re.S)
        links = re.findall(reg,self.content)

        return links
    def message(self):
        reg_link=re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)" href="(.*?)".*? <span class="t2">', re.S)
        reg_company='<span class="t2"><a target="_blank" title="(.*?)" href="(.*?)">.*?</a></span>'
        reg_area='<span class="t3">(.*?)</span>'
        reg_salary='<span class="t4">(.*?)</span>'
        reg_time = '<span class="t5">(.*?)</span>'

        link=re.findall(reg_link,self.content)
        company=re.findall(reg_company,self.content)
        area=re.findall(reg_area,self.content)
        salary=re.findall(reg_salary,self.content)
        time=re.findall(reg_time,self.content)
        #print(link[0][0])
        #print(company[0])
        #print(area)
        #print(salary)
        #print(time)
        info_dict={}
        
        for i in range(len(link)):
            info_dict[link[i][0]] = {'link':link[i][1],
                                     'company_name':company[i][0],
                                     'company_link':company[i][1],
                                     'area':area[i],
                                     'salary':salary[i],

                                     'time':time[i]}
        
        return info_dict

    def info(self):
        info_list=self.links
        info_dict={}
        for i in info_list:
            #print(i)
            con=requests.get(i,headers=self.header)
            con.encodint='gbk'
            htm=con.text
            skill_type = '<h1 title="(.*?)">'
            city='<p class="msg ltype" title="(.*?)&nbsp;'
            company_name='<p title=".*?">(.*?)</p>'
            company_size='<p class="at" title=".*?"><span class="i_people"></span>(.*?)</p>'
            company_type='<p class="at" title="(.*?)">\s*?<span class="i_trade">'
            company_description='<div class="tmsg inbox">\s*?([\S]*?)\s*?</div>'
            company_location='<span class="label">上班地址：</span>(.*?)\s*?</p>'
            salary='</h1>\s*?<strong>(.*?)</strong>'
            job_required='<div class="bmsg job_msg inbox">\s*?<p>(.*?)\s*?<div class="mt10">'
            experience_required='<span>\|</span>&nbsp;&nbsp;(.*?)&nbsp;&nbsp;<span>\|</span>'
            company_welfare='<div class="t1">\s*?<span class="sp4">([\S\W]*?)<div class="clear">'
            
            city=re.findall(city,htm)
            skill_type=re.findall(skill_type,htm)
            company_name=re.findall(company_name,htm)
            company_size=re.findall(company_size,htm)
            company_location=re.findall(company_location,htm)
            company_type=re.findall(company_type,htm)
            job_required=re.findall(job_required,htm)
            company_description=re.findall(company_description,htm)
            company_welfare=re.findall(company_welfare,htm)
            salary=re.findall(salary,htm)
            experience_required=re.findall(experience_required,htm)


            info_dict['company_name']={'city':city,
                                       'skill_type':skill_type,
                                       'company_location':company_location,
                                       'company_size':company_size,
                                       'company_type':company_type,
                                       'company_description':company_description,
                                       'job_required':job_required,
                                       'company_welfare':company_welfare,
                                       'salary':salary,
                                        'experience_required':experience_required}
        
        return info_dict
            
if __name__ =='__main__':
    url='https://search.51job.com/list/{},000000,0000,00,9,99,{},2,1.html'.format('010000','python')
    #x=QianCheng(url).links()
    #y=QianCheng(url).message()
    #print(x)
    #print(y)
    z=QianCheng(url).info()
    
    
    





    
