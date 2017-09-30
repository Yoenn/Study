# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Chrome("D:\Yoeng-\OneForAll\Selenium\Driver\chromedriver.exe")

driver.get('https://www.baidu.com')

print('baidu')

driver.quit()