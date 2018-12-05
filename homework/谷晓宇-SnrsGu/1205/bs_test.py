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

soup = BeautifulSoup(html_doc,'html.parser')

tag = soup.find(id = 'link3')  #返回值类似与字典
print(type(tag))
print(soup.find_all(id = 'link3'))

print(soup.find(id = 'link3').get('href'))
print(soup.find(id = 'link3')['href'])

#print(isinstance(a,dict))
print(soup.get_text())

print('xxxx',soup.select('.story'))
print(soup.select_one('.story'))   #list  查找结果就集合

print(soup.select_one('.story > #link1'))   #精确的一个    井号代表id，点代表class
print(type(soup.select_one('.story')))

print(soup.select_one('.story > a')) #也可以直接写标签
print(tag)
print(tag.name)


soup.select("body a")   #通过标签逐层查找
soup.select("html head title")


