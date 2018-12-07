from bs4 import BeautifulSoup
import bs4,requests,time

class JobSpider():

    def job_qc(self):
        for i in range(1):
            print('正在抓取{}页'.format(i+1))
            url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(i+1)
            # print(url)
            res = requests.get(url)
            if res.status_code == 200:
                res.encoding = 'gbk'
                soup = BeautifulSoup(res.text ,'html.parser')
                cententurls = soup.find_all('p',class_='t1')
                # for p in cententurls:
                #     print(p.a.get('href'))
                #     with open('urls.txt', 'a+') as f:
                #         f.write(p.a.get('href'))
                #         f.write('\n')
                # print(len(cententurls))
                # time.sleep(1)
                b = []
                for p in cententurls:
                    link = p.a.get('href')
                    b.append(link)
                return b
                # print(b)
    def job_link(self):
        b = self.job_qc()

        for y in b:
            # print('\n')
            # print('正在抓取这{}页'.format(y))

            html = requests.get(y)
            html.encoding='gbk'
            html = html.text
            div = BeautifulSoup(html, 'html.parser')
            title = div.h1.get('title')

            compay_name = div.select_one('a.catn').get('title')

            city = div.select_one('p.msg').text
            city = city.split('|')
            city = ' '.join([''.join(x.split()) for x in city])

            company_location = div.select_one('div.bmsg > p.fp').text

            company_info = div.select_one('div.tmsg').text

            company_welfare = div.select('div.t1 > span')
            company_welfare = ''.join([i.text.strip() for i in company_welfare])

            skills_required = div.select('p.fp > a')
            skills_required = ''.join([i.text.strip() for i in skills_required])

            job_required = div.select('div.inbox > p')[:12]
            job_required = ','.join([i.text.strip() for i in job_required])

            salary = div.select_one('div.cn > strong').text

            c=(title,compay_name,city,company_location.replace('\n',' ').replace('\t\t\t\t\t\t\t',' ').replace('\xa0\xa0\xa0\xa0\xa0\xa0\xa0',''),company_info.strip(),company_welfare,skills_required,job_required,salary)
            # print(c)

x = JobSpider()
x.job_link()
# x.job_qc()

