"""
@author:28646
@file: 2018.12.05前程无忧.py
@time: 2018/12/05
"""
from bs4 import BeautifulSoup
import requests

class QianCheng:

    def __init__(self,url='https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0',
                 encoding='gbk'):
        self.url = url
        self.encoding = encoding
        self.get_url = self.get_url()

    def get_url(self):
        '''
        获取网页内容
        :return: text文本
        '''
        res = requests.get(self.url)
        return res.text

    def info(self):
        '''
        分析text文档内容,提出有用的数据
        :return: 招聘数据列表
        '''
        if self.get_url.status_code == 200:
            soup = BeautifulSoup(self.get_url, 'html.parser')
            div = soup.find(class_='tHeader tHjob')
            salary = soup.select_one('div.cn > strong').text                #薪资
            company_name = soup.select_one('a.catn').get('title')           #公司名称
            city = soup.select_one('div.cn > p.msg.ltype').text             #城市
            city_list = city.split('|')
            city_list = [''.join(i.split()) for i in city_list]
            company_welfare = soup.select('div.cn > div > div > span')      #公司福利['五险一金', '员工旅游', '餐饮补贴', '通讯补贴', '定期体检', '周末双休', '免费班车', '年终奖金', '专业培训']
            company_welfare_list = []
            for i in company_welfare:
                company_welfare_list.append(i.text)

            job_required = soup.select('div.bmsg > p')                      #工作要求['1,5年以上开发经验，基本功扎实，精通Java；', '2,5年以上Linux经验，熟练使用常见命令与Shell脚本编程；', '3,熟悉主流开源框架，对Spring MVC、Spring Boot、Spring Cloud等有深入了解；', '4,熟练使用Maven或Gradle等构建工具；', '5,熟悉至少一种关系型数据库和至少一种非关系型数据库；', '6,熟悉Redis、memcached、RabbitMQ、RocketMQ等中间件产品；', '7,熟悉HTTP协议与RESTful架构风格，熟悉微服务架构；', '8,熟练使用Git，熟悉Pull Request工作流；', '9,对Docker有一定了解，能够独立编写Dockerfile、docker-compose配置文件；', '10,善于沟通，积极主动，有团队合作意识，有较强的分析问题、解决问题的能力；', ' ', '11,具有强烈的责任感，对产出负责。']
            job_required_list = []
            for i in job_required:
                job_required_list.append(i.text)

            company_type = soup.select('div.com_tag > p')                   #工作类型
            company_type_list = []
            for p in company_type:
                company_type_list.append(p.text)

            company_description = soup.select('div.tmsg')                   #公司描述
            company_description_list = []
            for q in company_description:
                company_description_list.append(q.text)

        print(city_list[0])
        print(salary)
        print(company_welfare_list)
        print(job_required_list[:-1])
        print(company_type_list[0])
        print(company_description_list[0])
        return [city_list[0],city_list[1],city_list[2],city_list[3],city_list[4],salary,company_welfare_list,job_required_list[:-1],
                company_type_list[0],company_type_list[1],company_type_list[2],company_description_list[0]]
if __name__ == '__main__':
    qiancheng = QianCheng()
    qiancheng.info()
