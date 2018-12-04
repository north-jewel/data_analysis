import requests

'''HEADERS = {
    # User-Agent(UA) 服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等。也就是说伪装成浏览器进行访问
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    # 用于告诉服务器我是从哪个页面链接过来的，服务器基此可以获得一些信息用于处理。如果不加入，服务器可能依旧会判断为非法请求
    'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&gx=&isSchoolJob=1&city=%E5%B9%BF%E5%B7%9E'
}
'''
class Retractor_net:
    def __init__(self,polis='北京',pk=1):
        self.polis = polis
        self.pk = pk
    def Out_url(self):
        HEADERS = {'Referer': 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        out_url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false'.format(self.polis)
        for pg in range(0,self.pk+1):
            from_data = {'first': 'true','pn': pg,'kd': 'python'}
            out_info = requests.post(out_url,data=from_data,headers=HEADERS)
            for i in range(len(out_info.json()['content']['positionResult']['result'])):
                url_info = out_info.json()['content']['positionResult']['result'][i]
                positionId = out_info.json()['content']['positionResult']['result'][i]['positionId']
                workYear = url_info['workYear']
                education = url_info['education']
                firstType = url_info['firstType']
                city = url_info['city']
                positionAdvantage =url_info['positionAdvantage']
                salary = url_info['salary']
                positionName = url_info['positionName']
                companySize = url_info['companySize']
                financeStage = url_info['financeStage']
                jobNature =url_info['jobNature']
                district = url_info['district']
                companyFullName = url_info['companyFullName']
                print(positionId)
                print(url_info)
if __name__ == '__main__':
    Retractor_net().Out_url()


