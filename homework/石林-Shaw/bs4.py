from bs4 import BeautifulSoup
import bs4
import requests

class Job():
    def __init__(self,url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0',encoding = 'gb2312'):
        self.url = url
        self.encoding = encoding

    def requests(self):
        res = requests.get(self.url)
        res.encoding = self.encoding
        html = res.text

        return html

    def info(self):
        res = self.requests()
        soup = BeautifulSoup(res, 'html.parser')
        project_name = soup.select_one('h1').text
        company_name = soup.select_one('a.catn').get('title')
        company_type = soup.select_one('p.at').get('title')
        company_people = soup.select('div.com_tag > p')[1].text
        company_project = soup.select('div.com_tag > p')[2].text
        slary = soup.select_one('div.cn > strong').text
        welfare = soup.find('div',class_ = 't1').text.strip()
        zhiwei_info = soup.find('div',class_ = 'bmsg job_msg inbox').text.strip()
        location = soup.select_one('div.bmsg > p.fp').text
        company_info = soup.select_one('div.tBorderTop_box > div.tmsg').text
        experience = soup.select_one('p.msg').text.strip()
        city = str(experience).split('|')[0]
        experiences = str(experience).split('|')[1]
        edu_required = str(experience).split('|')[2]

        return (project_name,company_name,company_type,company_people,company_project,slary,welfare,zhiwei_info,location,company_info,city,experiences,edu_required )


if __name__ =='__main__':
    A = Job().info()
