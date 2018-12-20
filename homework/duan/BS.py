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

print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('p'))  
print('*'*18)
print(soup.findAll('p'))  
print(soup.find_all('p',class_ = 'title'))  #class后加下划线
print(soup.find_all(class_ = 'sister')) #class中加的是属性名

print(soup.find_all(id = 'link3')) 


print(soup.find(id = 'link3').get('hre'))  #直接获取（href）的值
print(soup.find(id= 'link3')['href'])


strl = 'aaa'
print(isinstance(strl,(str,int)))  
print(isinstance(strl,object))



print(soup.select('.story'))  #class名
print(soup.select('#link3'))  #id名
print(soup.select_one('.story'))
print(soup.select_one('#link3'))
