# -*- coding:utf-8 -*-

from lxml import etree


text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html" class="bold">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
print(result)

# html = etree.parse('hello.html')
# result = etree.tostring(html, pretty_print=True)
# print(result)

print type(html)
result = html.xpath('//li')
print result
print len(result)
print type(result)
print type(result[0])

result = html.xpath('//li/@class')
print result

result = html.xpath('//li/a[@href="link1.html"]')
print result

result = html.xpath('//li//a')
print result

result = html.xpath('//li/a//@class')
print result

result = html.xpath('//li[last()]/a/@href')
print result

result = html.xpath('//li[last()-1]/a')
print result[0].text

result = html.xpath('//*[@class="bold"]')
print result[0].tag




