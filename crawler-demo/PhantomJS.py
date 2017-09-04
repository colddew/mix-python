# -*- coding:utf-8 -*-

from selenium import webdriver


driver = webdriver.PhantomJS()
driver.implicitly_wait(40)
driver.get("http://duorou.com/duorou-qiuli-1202.html")
li = driver.find_element_by_xpath("//dd[@class='goods_w']//li[last()]")
li.click()
print driver.find_element_by_id('goods_price').text
# time.sleep(60)
driver.close()
