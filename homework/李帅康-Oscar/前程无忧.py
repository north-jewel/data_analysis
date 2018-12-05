import requests
from bs4 import BeautifulSoup


class Analyzer():
    def __init__(self,url = 'https://jobs.51job.com/shenzhen-ftq/108974685.html?s=01&t=0',encoding = 'gb2312'):
        self.url = url
        self.encoding = encoding


    def requests(self):
        res = requests.get(self.url)
        res.encoding = self.encoding
        html = res.text

        return html


    def info(self):
        html = self.requests()
        soup = BeautifulSoup(html, 'html.parser')
        city = soup.select_one('p.msg').text.split('|')[0].strip()
        skill_type = soup.find('h1').text.strip()
        company_name = soup.select_one('a.catn').text.strip()
        company_size = soup.select('p.at')[1].get('title')
        company_type = soup.select('p.at')[2].get('title')
        company_description = soup.select_one('div.tmsg').text.strip()
        company_location = soup.find_all('p',class_ = 'fp')[2].text.strip()
        job_required = ','.join([i.text for i in soup.select('.job_msg > p')])
        edu_required = soup.select_one('p.msg').text.split('|')[2].strip()
        experience_required = soup.select_one('p.msg').text.split('|')[1].strip()
        company_welfare = soup.select('.cn > strong')[0].text

        return (city,skill_type,company_name,company_size,company_type,company_description,company_location,
                job_required,edu_required,experience_required,company_welfare)

if __name__ == '__main__':
    a = Analyzer().info()

#city 城市  skill_type 技术类型 company_name 公司名  company_size 公司大小 company_type  公司类型
#company_description 公司简介  company_location 公司位置 job_required 职位要求 skills_required 技能要求
#edu_required 学历需求  experience_required  经验要求  company_welfare  公司福利