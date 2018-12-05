# -*- coding: utf-8 -*-
"""
   File Name：     bsstudy
   Product:        PyCharm
   Project:    python4
   File:       bsstudy.py
   Author :       ZXR
   date：          2018/12/5
   time:           10:19
"""
import bs4
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
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

print(soup.title)    #<title>The Dormouse's story</title>
print(soup.title.name)  #title
print(type(soup.title.text))  #The Dormouse's story    #type:<class 'str'>
print(type(soup.title.string))  #The Dormouse's story   #type:<class 'bs4.element.NavigableString'>
print('*'*100)
print(soup.find('p'))
print(soup.find_all('p')[0])
print('*'*100)
print(soup.find_all('p'))
print(dir(soup.find_all(class_='story')))
print(soup.find(id='link3'))
print(soup.find(id='link3').get('href'))
print(soup.find(id='link3')['href'])
print(isinstance(soup.find(id='link3'),dict))
print(issubclass(bs4.element.Tag,dict))
