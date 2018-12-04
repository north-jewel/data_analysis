import urllib.parse

class method:
    def read_file(self,path,arg='utf-8',evals=False):

        with open(path,'r',encoding=arg) as f :
            if evals:
                a=eval(f.read())
                return a
            else:
                a=f.read()

                return a
    def convert(self,dict):
        #key=dict.keys()
        #value=dict.values()
        new_dict={}
        for i ,x in dict.items():
            new_dict[x]=i
        return new_dict

    def isChinese(self,str_):
        str1=''
        for c in str_:
            if ('\u4e00' <= c <= '\u9fa5'):
                str1+=c
        return str1
        #return False
    def isEnglish(self,str_):
        english=''
        for i in str_:
            if not ('\u4e00' <= i <= '\u9fa5'):
                english+=i
        return english
    def decods(self,str_):
        str1=urllib.parse.quote(str_)
        return str1
    def encods(self,str_):
        str_1=urllib.parse.unquote(str_)
        return str_1
    def add_city(self,city):
        list_1 = city.split(',')
        return list_1
    def writes(self,name,text,arg):
        with open(name,'w',encoding=arg) as f:
            f.write(text)
if __name__ == "__main__":
    m=method()
    b=m.add_city('dsfsd,sdfsd,fsdf')
    print(b)
