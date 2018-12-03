import requests

import re

class Spider():
    
    def __init__(self,
                 url='https://www.x23us.com/html/70/70640/',
                 charset='gbk',
                 json = None,

                 ):

        self.url = url
        self.json = json
        self.charset = charset
        self.html = self.html()

    def html(self):

        res = requests.get(self.url)
        res.encoding = self.charset

        if self.json != None:
            return res.json()

        return res.text

    def info(self, **regex):

        info_dict = {}

        for key,value in regex.items():

            info_dict[key] = re.findall(value,self.html)[:3]
        # print(info_dict)
        return info_dict

    def iter_info(self, **regex):
        info_dict = {}

        for key, value in regex.items():
            info_dict[key] = re.finditer(value, self.html)
        # print(info_dict)
        return info_dict


            
if __name__ == '__main__':
    x = Spider('https://jobs.51job.com/beijing-cyq/104283209.html?s=01&t=0',charset='gbk')
    info = x.info(skill_type = '<h1 title="(.*?)">',
                  city='<p class="msg ltype" title="(.*?)&nbsp;',
                  company_name='<p title=".*?">(.*?)</p>',
                  company_size='<p class="at" title=".*?"><span class="i_people"></span>(.*?)</p>',
                  company_type='<p class="at" title="(.*?)">\s*?<span class="i_trade">',
                  company_description='<div class="tmsg inbox">\s*?([\S]*?)\s*?</div>',
                  company_location='<span class="label">上班地址：</span>(.*?)\s*?</p>',
                  salary='</h1>\s*?<strong>(.*?)</strong>',
                  job_required='<div class="bmsg job_msg inbox">\s*?<p>(.*?)\s*?<div class="mt10">',
                  experience_required='<span>\|</span>&nbsp;&nbsp;(.*?)&nbsp;&nbsp;<span>\|</span>',
                  company_welfare='<div class="t1">\s*?<span class="sp4">([\S\W]*?)<div class="clear">',
                  )
    print(info)





















    
