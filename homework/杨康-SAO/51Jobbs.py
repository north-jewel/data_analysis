from job_spider import *
from argfile import *
from bs4 import BeautifulSoup

class JobSpider:
    def __init__(self, area_word, key_word):
        self.area_word = area_word
        self.key_word = key_word
        self.job_url_list = self.spider_51Job()



    def spider_51Job(self):
        area_word = list(area.keys())[list(area.values()).index(self.area_word)]
        job_url = 'https://search.51job.com/list/{},000000,0000,01,9,99,{},2,1.html?'.format(area_word, self.key_word,)
        job_obj = Spider(url=job_url)
        job_text = job_obj.html5()
        #print(job_text)
        soup = BeautifulSoup(job_text, 'html.parser')
        soup = soup.find_all('p', class_='t1')
        job_url_list = []
        for i in soup:
            job_url_list.append(i.a.get('href'))

        return job_url_list




    def job_info(self):
        job_dict = {}
        job_dict_list = []
        for index in range(5):
            job_obj = Spider(url=self.job_url_list[index])
            job_text = job_obj.html5()
            soup = BeautifulSoup(job_text, 'html.parser')
            skill_type = soup.h1.text.strip()
            print(skill_type)
            city = soup.find('p', class_='msg ltype').text.strip().split('|')[0]

            company_name = soup.find('div', class_='com_msg').text.strip()

            company_size = soup.select('div.com_tag > p')[1].text

            company_type = soup.select('div.com_tag > p')[2].text.strip()

            company_description = soup.find('div', class_='tmsg inbox').text.strip()
            try:
                company_locationa = soup.find('div', class_='bmsg inbox').text
            except AttributeError:
                company_location = None
            else:
                company_location = company_locationa.replace('地图','').strip()

            salary = soup.select_one('div.cn > strong').text

            g = soup.find('div', class_='mt10').text
            job_required = soup.find('div',class_='bmsg job_msg inbox').text.replace(g,'').replace('微信分享','').strip()

            experience_required = soup.find('p', class_='msg ltype').text.strip().split('|')[1]

            company_welfare = soup.find('div', class_='t1').text.strip()

            job_dict[self.key_word] = {'skill_type': skill_type,
                                       'city': city,
                                       'company_name': company_name,
                                       'company_size': company_size,
                                       'company_type': company_type,
                                       'company_description': company_description,
                                       'company_location': company_location,
                                       'salary': salary,
                                       'job_required': job_required,
                                       'experience_required': experience_required,
                                       'company_welfare': company_welfare,}
            job_dict_list.append(job_dict[self.key_word])
        return job_dict_list







if __name__ == '__main__':
    x = JobSpider('北京', 'python')
    #n = x.spider_51Job()
    #print(n)
    a = x.job_info()
    print(a)
