def get_page_source(self,
                    url,
                    encoding = 'UTF-8'):
    s = requests.Session()
    res_obj = s.get(url,headers = self.header)
    if res_obj.status_code == 200:
        res_obj.encoding = encoding
        print(res_obj.text)
        regex = '<script>window.location.href=(.*?);</script>'
        new_url = re.findall(regex,res_obj.text)[0]
        print(new_url)
        new_url = eval(new_url)
        new_obj = s.get(new_url,headers = self.header)
        if new_obj.status_code == 200:
            new_obj.encoding = encoding
            return new_obj.text
        else:
            print('2,新链接请求失败！')
            return None
    else:
        print('1,原链接请求失败！')
        return None
get_page_source()
