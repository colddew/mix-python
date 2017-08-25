# -*- coding:utf-8 -*-

# Selenium 2 is WebDriver

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WebDriver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")
        self.assertIn(u'百度一下，你就知道', driver.title)
        elem = driver.find_element_by_name("wd")
        elem.send_keys("python")
        elem.send_keys(Keys.RETURN)
        # print driver.page_source
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    # browser = webdriver.Chrome()
    # browser.get('http://www.baidu.com/')
    unittest.main()
