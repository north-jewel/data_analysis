import requests,re
# url='https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# info = requests.get(url,headers).content.decode('gbk')
# print(info)
class Jobs:
    def __init__(self):
        pass
    def Out_url(self):
        out_url ='https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        headers = {'Referer': 'https://www.51job.com/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        out_info = requests.get(out_url,headers=headers).content.decode('gbk')

        re_company_name = '<span class="t2"><a target="_blank" title="(.*?)" href="(.*?)">(.*?)</a></span>'
        re_area = '<span class="t3">(.*?)</span>'
        re_salary = '<span class="t4">(.*?)</span>'
        re_value = '<input class="checkbox" type="checkbox" name="delivery_jobid" value="(.*?)" jt="0" style="display:none" />'

        company_name=re.findall(re_company_name,out_info)
        salary = re.findall(re_salary,out_info)
        value = re.findall(re_value,out_info)
        for i in range(len(value)):
            spell = 'https://jobs.51job.com/beijing-xcq/{}.html'.format(value[i])
            print(spell)


Jobs().Out_url()





