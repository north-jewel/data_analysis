from bs4 import BeautifulSoup
import bs4
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
<a class="story">fsfsf</a>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# # print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.title.string)
# print(type(soup.title.text)) # <class 'str'>
# print(type(soup.title.string)) # <class 'bs4.element.NavigableString'>
# # print(soup.p)
# print(soup.find('p'))
# print(soup.find_all('p'))
# print(type(soup.find_all('p'))) # <class 'bs4.element.ResultSet'> ,可以近似的当成list来用
# print('*'*20)
# print(soup.find_all('p')[0])
# print(soup.findAll('p'))
# print('a标签')
#
# print(type(soup.find('p')))
# print(type(soup.find_all('p')[0]))
# print(dir(soup.find('p')))
# # print(soup.find('p').attrs)
# soup.find_all('p',class_='title')
print('*******')
# print(soup.find_all(class_='story'))
print(soup.find(id="link3"))
print(type(soup.find(id="link3")))  # <class 'bs4.element.Tag'>  类似于字典
print(soup.find(id="link3").get('hre'))
# print(soup.find(id="link3")['hre'])
# print(soup.find(id="link3"))
str1='sss'
print(isinstance(str1,object))
# print(isinstance(soup.find(id="link3"),dict))
print(issubclass(bs4.element.Tag,dict))
# soup.find_all('p',class_='title')
# print(soup.select('.title'))
# print(type(soup.select('.title')))
# print(soup.select_one('.title'))
# print(type(soup.select('.story')))
# print(soup.select('.story'))
# print(soup.select_one('.story'))

print(soup.select_one('#link1'))






