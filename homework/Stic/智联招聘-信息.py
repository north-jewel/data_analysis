import requests,re,json,time,random
from openpyxl import load_workbook

def sprid(url):
    # proxies = {'http': '182.88.15.219', 'https': '182.88.15.219'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    return json.loads(res.text)
# txt = sprid('https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=530&industry=10100&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&rt=cb3d2dc85c7b4a9998c7d1f77b348a12&_v=0.39734715&x-zp-page-request-id=dab284be150a45f5b5f1175276fa3a36-1543667240764-55123')
city = [530,538,765,763,531,801]
city2 = ['北京','上海','深圳','广州','天津','成都']
rows = ['B','C','D','E','F','G','H','I','J','K','L','M']
fair = {}
def grab_p(page,x):
    print(page,x)
    txt = sprid(
        'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId={}&industry=10100&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&rt=cb3d2dc85c7b4a9998c7d1f77b348a12&_v=0.48911627&x-zp-page-request-id=39391449c3b44a079ff5defc126ccb37-1543837658799-897959'.format(page,x))
    for i in range(len(txt['data']['results'])):
        fair['{}{}'.format(city2[city.index(x)],i*(page+1))]=[txt['data']['results'][i]['jobType']['display'],
                 txt['data']['results'][i]['company']['name'],
                 txt['data']['results'][i]['company']['size']['name'],
                 txt['data']['results'][i]['company']['type']['name'],
                                                     'None',
                 txt['data']['results'][i]['city']['display'],
                 txt['data']['results'][i]['jobName'],
                 txt['data']['results'][i]['emplType'],
                 txt['data']['results'][i]['eduLevel']['name'],
                 txt['data']['results'][i]['workingExp']['name'],
                 '{}'.format(txt['data']['results'][i]['welfare']),
                 txt['data']['results'][i]['salary'],
                 ]
    return fair
for x in city:
    txt = sprid(
        'https://fe-api.zhaopin.com/c/i/sou?&pageSize=60&cityId={}&industry=10100&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&rt=cb3d2dc85c7b4a9998c7d1f77b348a12&_v=0.48911627&x-zp-page-request-id=39391449c3b44a079ff5defc126ccb37-1543837658799-897959'.format(x))
    page = int(txt['data']['numFound'])//60+1
    print(page)
    for i in range(page):
        grab_p(i,x)
        s = random.randint(2,6)
        time.sleep(s)
recriut = load_workbook('33.xlsx')
sheet = recriut['Sheet1']
print(fair)
for k,v in fair.items():
    sheet['{}{}'.format('A', list(fair.keys()).index(k) + 2)].value = k
    for r in rows:
        sheet['{}{}'.format(r,list(fair.keys()).index(k)+2)].value = fair[k][rows.index(r)]

recriut.save('33.xlsx')

'''
x = open('province.txt')
province_list = []
for i in x:
    province_list.append(i)
print(province_list[0])
'''

