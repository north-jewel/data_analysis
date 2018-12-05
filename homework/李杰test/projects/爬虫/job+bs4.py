from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

url = 'https://jobs.51job.com/beijing-sjsq/108942405.html?s=01&t=0'
html_doc = requests.get(url,headers=headers).text



class Bs4test:
    def __init__(self,url):
        self.url = url
    def Company_code(self):
        html_doc = requests.get(self.url, headers=headers).text
        return html_doc
    def Company_info(self):
        soup = soup = BeautifulSoup(self.Company_code(),'html.parser')

        title = soup.find(class_='cn').h1.get('title')
        title_2 = soup.find('h1').text.strip()
        print(title)

        company = soup.find(class_='catn').text.strip()
        company_2 = soup.find(class_='catn').get('title')
        company_3 = soup.find()
        print(company_2)

        company_url = soup.find(class_='catn').get('href')
        print(company_url)

        company_weafer = soup.find_all(class_='sp4')
        welfare =[]
        for i in company_weafer:
            welfare.append(i.text.strip())
        print(welfare)

        company_re = soup.find(class_='bmsg job_msg inbox').find_all('p')
        ask_for = []
        for i in company_re:
            ask_for.append(i.text.strip())
        print(ask_for)

        company_post = soup.find(class_='msg ltype').text.strip()
        print(company_post.replace('|',''))

        monthly_pay = soup.find(class_='rjlist r3').find_all('strong')[0].text
        print(monthly_pay)

        company_address = soup.find(class_='bmsg inbox').find(class_='fp').text
        company_address_2 = soup.select('div.tCompany_main > div:nth-of-type(2) > div > p')[0].text.strip()
        #print(company_address)
        print(company_address_2)

        company_message = soup.find(class_='tmsg inbox').text.strip()
        print(company_message)

        company_message_2 = soup.find(class_='com_tag').find_all('p')
        message = []
        for i in company_message_2:
            message.append(i.text.strip())
        print(message)

        return 'over'


print(Bs4test(url).Company_info())

















