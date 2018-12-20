from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'lxml')

soup.prettify()  #输出bs对象解析的代码
#type = str

soup.title  #输出bs对象的这个标签（只返回第一个）
#type = Tag

soup.body.name  #返回这个标签的名字，如<a>标签的名字就叫a
#type = str

soup.title.string  #返回这个标签的内容，就是开始和结束标签中间的字
#type = NavigableString （可以直接str）

soup.title.parent.name  #返回这个标签的父级标签名称,如此处的title的父级标签是<head>
#type = str  

soup.p['class']  #返回这个p标签的class属性的值，也可以使用.get('class')效果一样，
              #注意这里  据我所知  只有索引class ，rel , rev , accept-charset , headers , accesskey的时候返回的是一个列表，因为这个属性的值可能会有两个（以空格分隔）列表中是一个str表示这个属性的值
              #如果直接索引其他属性则直接返回str（不懂自行尝试）#详见官网（多值属性） https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
#type = list

soup.find_all('a')  #返回bs对象中所有的a标签在一个Tag对象的集合中
#type = ResultSet

soup.find('a') #返回bs对象的这个标签（只返回第一个），与上述第22行效果一致
#type = Tag

soup.find(id="link3") #返回第一个标签属性id值为link3的标签
#type = Tag

soup.find('a',id = 'link3') #在所有a标签中寻找标签属性id为link3的标签
#type = Tag

tag = soup.a
tag['id'] #表示一个Tag对象（标签）索引这个属性，返回该属性对应的值，与上述第34行效果一样
#type = str

soup.get_text() #获取这个bs对象中的所有文字内容,不懂打印这行代码
#type = str

print('-'*50)

a = soup.p      #获取soup中的第一个p标签赋值给a 此时a的类型为Tag类型
print(a.name)   #打印a此时的name
a.name = 'A'    #改变a的名称
print(a.name)   #打印改变后a的名字
print(a)        #打印此时的a
print(soup.p)   #获取soup中的第一个p标签，此时的第一个p标签就不是刚才的了，因为刚才的p标签被改变了
    #结论，改变一个标签的name时，该会影响到soup中该标签的name，且这个标签就会被改变

print('-'*50)

soup.select('a') #返回一个列表，列表中是soup中的所有a标签
#type = list

soup.select_one('a') #soup中第一个a标签   注：select和select_one方法都不支持上述45与48行的操作
#type = Tag

soup.select('p > a') #返回p标签下的所有a标签  select_one同理只不过是返回第一个
#type = list

soup.select_one('p > a:nth-of-type(2)') #返回p标签下的第二个a标签，
                                            #select也有这种操作，只不过返回一个列表
#type = Tag                                 #网页复制的（nth-child）修改为（nth-of-type）



#（#rso > div > div:nth-child(1) > div > div.rc）
# 这个表示id为rso标签  >  div标签  >  第一个div标签  >  div标签  >  class为rc的div标签
# 最后锁定在class为rc的div标签使用select方法查找的时候返回包括这个标签下的所有内容
#  # 代表id    . 代表class
