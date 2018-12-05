from job_spider import *
from argfile import *
import re
import numpy as np
class JobSpider:
    def __init__(self, area_word, key_word):
        self.area_word = area_word
        self.key_word = key_word
        self.job_dict = self.spider_51Job()



    def spider_51Job(self):
        area_word = list(area.keys())[list(area.values()).index(self.area_word)]
        page_url = 'https://search.51job.com/list/{},000000,0000,01,9,99,{},2,1.html?'.format(area_word, self.key_word)
        #print(page_url)
        regx = re.compile(r'class="t1 ">.*? <a target="_blank" title=".*?" href="(.*?)".*? <span class="t2">', re.S)
        #page_re = '<span class="og_but" onclick="jumpPage\((.*?)\);">'

        #page_obj = Spider(url=page_url)
        #job_dict = job_obj.iter_info(job_url=regx, )
        #page_info = page_obj.info(page=page_re,)
        job_url_list = []
        job_list = []
        #page = page_info['page'].replace('\'', '')
        page = 2
        for i in range(int(page)):
            i += 1
            job_url = 'https://search.51job.com/list/{},000000,0000,01,9,99,{},2,{}.html?'.format(area_word, self.key_word, i)
            #print(job_url)
            job_url_list.append(job_url)
        for index in range(len(job_url_list)):
            job_obj = Spider(url=job_url_list[index])
            job_dict = job_obj.iter_info(job_url=regx,)
            #print(job_dict)
            job_list.append(job_dict)

        return job_list



    def job_info(self):
        job_info_list = []
        for i in range(len(self.job_dict)):
            while True:
                try:
                    job_info_dict = {}
                    job_url = next(self.job_dict[i]['job_url']).group(1)
                    skill_type = '<h1 title="(.*?)">'
                    city = '<p class="msg ltype" title="(.*?)&nbsp;'
                    company_name = '<p title=".*?">(.*?)</p>'
                    company_size = '<p class="at" title=".*?"><span class="i_people"></span>(.*?)</p>'
                    company_type = '<p class="at" title="(.*?)">\s*?<span class="i_trade">'
                    company_description = '<div class="tmsg inbox">\s*?([\S]*?)\s*?</div>'
                    company_location = '<span class="label">上班地址：</span>(.*?)\s*?</p>'
                    salary = '</h1>\s*?<strong>(.*?)</strong>'
                    job_required = '<div class="bmsg job_msg inbox">\s*?<p>(.*?)\s*?<div class="mt10">'
                    experience_required = '<span>\|</span>&nbsp;&nbsp;(.*?)&nbsp;&nbsp;<span>\|</span>'
                    company_welfare = '<div class="t1">\s*?<span class="sp4">([\S\W]*?)<div class="clear">'


                    info_obj = Spider(url=job_url)
                    info_dict = info_obj.info(skill_type=skill_type,
                                              city=city,
                                              company_name=company_name,
                                              company_size=company_size,
                                              company_type=company_type,
                                              company_description=company_description,
                                              company_location=company_location,
                                              salary=salary,
                                              job_required=job_required,
                                              experience_required=experience_required,
                                              company_welfare=company_welfare,

                                              )
                except StopIteration:
                    return job_info_list
                else:
                    job_info_dict[self.key_word] = info_dict

                    job_info_list.append(job_info_dict)




if __name__ == '__main__':
    x = JobSpider('北京', 'python')
    #n = x.spider_51Job()
    #print(n)
    a = x.job_info()
    print(len(a))
