# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
from lxml import etree

# doc = pq(filename='hello.html')
# doc = pq("<html></html>")
# doc = pq(etree.fromstring("<html></html>"))
# doc = pq('http://www.baidu.com')

html = """
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
"""

doc = pq(etree.fromstring(html))
print doc.html()
print type(doc)
li = doc('li')
print type(li)
print li.text()

p = pq('<p id="hello" class="hello"></p>')('p')
print p.attr("id")
print p.attr("id", "plop")
print p.attr("id", "hello")

p = pq('<p id="hello" class="hello"></p>')('p')
print p.addClass('beauty')
print p.removeClass('hello')
print p.css('font-size', '16px')
print p.css({'background-color': 'yellow'})

p = pq('<p id="hello" class="hello"></p>')('p')
print p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>')
print p.prepend('Oh yes!')
d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
p.prependTo(d('#test'))
print p
print d
d.empty()
print d

doc = pq(html)
lis = doc('li')
for li in lis.items():
    print li.html()

print lis.each(lambda e: e)

print pq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'})
print pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True)
