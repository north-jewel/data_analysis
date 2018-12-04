import re,requests,json


class ZhaoPin:
    def __init__(self,headers,out_url):
        self.header = headers
        self.outer_url = out_url
    def Outer_url(self):
        outer_info = requests.get(self.outer_url,headers=self.header)
        json_response = outer_info.content.decode()
        dict_json = json.loads(json_response)
        #print(dict_json['data']['results'][1]['jobType']['items'])
        #for i in range(len(dict_json['data']['results'])):
        print(dict_json['data']['results'][1])
        for i in range(2):
            corporation_url = dict_json['data']['results'][i]['positionURL']#公司url
            interior_info = requests.get(corporation_url,headers=self.header).text
            re_list_info = '<span>(.*?)</span>'
            re_city = '<span><a target="_blank" href="(.*?)">(.*?)</a></span>'
            re_skill_type = '<h1 class="l info-h3">(.*?)</h1>'
            re_monthly_pay = '<strong>(.*?)元/月</strong>'
            re_company_size = '<strong>(.*?)人</strong>'
            re_company_type = '<li><span class="iconfont icon-promulgator-type"></span><strong>(.*?)</strong></li>'
            #re_company_name = '<a rel="nofollow" href="(.*?)" target="_blank">(.*?)</a>'


            list_info = re.findall(re_list_info,interior_info)[4:7]
            city = re.findall(re_city,interior_info)[0][1]
            skill_type = re.findall(re_skill_type,interior_info)[0]
            monthly_pay = re.findall(re_monthly_pay,interior_info)[0]
            company_size = re.findall(re_company_size,interior_info)
            company_type = re.findall(re_company_type,interior_info)[0]
            #company_name = re.findall(re_company_name,interior_info)[0][1]
            print(len())
        return 1

if __name__ == '__main__':

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    for i in range(5):
        out_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&at=cb61f0195d5c4ebb8f41a288ae4f73f6&rt=cb54cccaa3284157b54994180426de07&_v=0.54601367&userCode=715503136&x-zp-page-request-id=47844301be274cf18e3174a25ed98a1f-1543631003376-851087'.format(60*i)
        print(out_url)
    #ZhaoPin(headers,out_url).Outer_url()