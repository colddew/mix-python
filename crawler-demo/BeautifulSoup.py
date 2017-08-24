# -*- coding:utf-8 -*-

import re
from bs4 import BeautifulSoup, Comment


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print soup.prettify()

print soup.title
print soup.head
print soup.a
print soup.p

print soup.p.name
print soup.p.attrs
print soup.p['class']
print soup.p.string

print soup.a
print soup.a.string
print type(soup.a.string)

if type(soup.a.string) == Comment:
    print soup.a.string

print soup.head.contents
print soup.head.contents[0]

print soup.head.children
for child in soup.body.children:
    print child

for string in soup.strings:
    print repr(string)

for string in soup.stripped_strings:
    print repr(string)

print soup.find_all('a')

for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

print soup.find_all(["a", "b"])

print soup.p.has_attr('class')

print soup.find_all(id='link2')
print soup.find_all(href=re.compile("elsie"))
print soup.find_all(href=re.compile("elsie"), id='link1')
print soup.find_all("a", class_="sister")
# print data_soup.find_all(attrs={"data-foo": "value"})

print soup.select('title')
print soup.select('.sister')
print soup.select('#link1')
print soup.select('p #link1')
print soup.select("head > title")
print soup.select('a[class="sister"]')
print soup.select('a[href="http://example.com/elsie"]')
print soup.select('p a[href="http://example.com/elsie"]')

print type(soup.select('title'))
print soup.select('title')[0].get_text()

for title in soup.select('title'):
    print title.get_text()
