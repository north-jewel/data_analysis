
import requests
from bs4 import BeautifulSoup

class Result:
    def __init__(self, url='https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0',
                 ):
        res = requests.get(url)
        self.soup = BeautifulSoup(res.text, 'html.parser')

    def company_name(self):

        company_name = self.soup.select_one('a.catn').get('title')
        return company_name
    # 工作需求

    def job_required(self):
        job_required = self.soup.select('div.inbox > p')[:12]
        job_required = [i.text.strip() for i in job_required]
        job_required = [''.join(i.split()) for i in job_required if len(i) != 0]
        return job_required
    # 公司位置

    def company_location(self):
        company_location = self.soup.select_one('div.bmsg > p.fp').text
        return company_location
    # 学历要求

    def edu_required(self):
        edu_required = self.soup.select_one('p.msg').text
        edu_required = edu_required.split('|')
        edu_required = ["".join(i.split()) for i in edu_required]
        return edu_required
    # 公司描述

    def company_description(self):
        company_description = self.soup.select('p.at')
        return company_description
    # 公司类型

    def company_type(self):
        company_description = self.company_description()
        company_type = company_description[0].text
        return company_type
    # 公司规模

    def company_size(self):
        company_description = self.company_description()
        company_size = company_description[1].text
        return company_size
    # 技能类型

    def skill_type(self):
        company_description = self.company_description()
        skill_type = [i.text.strip() for i in company_description[2:4]]
        return skill_type

if __name__ == '__main__':
    r = Result()


