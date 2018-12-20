import requests
import json
import csv
import glob

class Jd:
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    def __init__(self,
                 url='https://wqcoss.jd.com/mcoss/secondkill/show?callback=jsonCBSeckillItem&pretime=1542362401&count=60&offset=0&actid=114299&ctx=&g_tk=5381&g_ty=ls'
                 ):
        self.url = url#时间链接
        self.html = self.get_text()
        self.text = self.jd_json()

    def get_text(self):
        s = requests.get(self.url, headers=self.header)
        #print(s.text)
        html = json.loads(s.text.replace('jsonCBSeckillItem(', '').replace(');', '')[:-1])['data']['list']
        return html



    #名称、图片、现价、原价
    def jd_json(self):
        jd = {}
        name = []
        img = []
        chprice = []
        pcprice = []
        for i in self.html:
            name.append(i['skuname'])   
            img.append('https://img10.360buyimg.com/mobilecms/s200x200_{}!q70.dpg'.format(i['imgbase']))
            chprice.append(i['chprice'])
            pcprice.append(i['pcprice'])
        jd['name'] = name
        jd['img'] = img
        jd['chprice'] = chprice
        jd['pcprice'] = pcprice
        return jd

    def save_csv(self):
        if not glob.glob('jd.csv'):
            csv_file = open('jd.csv', 'w', newline='')
            writer = csv.writer(csv_file)
            writer.writerow(['name', 'img', 'chprice', 'pcprice'])
            self.text = self.jd_json()
            text = zip(self.text['name'], self.text['img'], self.text['chprice'], self.text['pcprice'])
            for i in text:
                writer.writerow(list(i))
        else:
            csv_file = open('jd.csv', 'a', newline='')
            writer = csv.writer(csv_file)
            self.text = self.jd_json()
            text = zip(self.text['name'], self.text['img'], self.text['chprice'], self.text['pcprice'])
            for i in text:
                writer.writerow(list(i))

Jd('https://wqcoss.jd.com/mcoss/secondkill/show?callback=jsonCBSeckillItem&pretime=&count=60&offset=0&actid=114299&ctx=&g_tk=5381&g_ty=ls').save_csv()
Jd('https://wqcoss.jd.com/mcoss/secondkill/show?callback=jsonCBSeckillItem&pretime=1542520801&count=60&offset=0&actid=114299&ctx=&g_tk=5381&g_ty=ls').save_csv()
Jd('https://wqcoss.jd.com/mcoss/secondkill/show?callback=jsonCBSeckillItem&pretime=1542528001&count=60&offset=0&actid=114299&ctx=&g_tk=5381&g_ty=ls').save_csv()
Jd('https://wqcoss.jd.com/mcoss/secondkill/show?callback=jsonCBSeckillItem&pretime=1542542401&count=60&offset=0&actid=114299&ctx=&g_tk=5381&g_ty=ls').save_csv()
Jd('https://wqcoss.jd.com/mcoss/secondkill/show?callback=jsonCBSeckillItem&pretime=1542549601&count=60&offset=0&actid=114299&ctx=&g_tk=5381&g_ty=ls').save_csv()





