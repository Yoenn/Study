#-*-coding: utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path = "D:\Yoeng-\OneForAll\Selenium\Driver\geckodriver.exe")

driver.get('file:///C:/Users/oliverchan/Desktop/uploadFiles/upload.html')

print('打开网页')

driver.find_element_by_name('file').send_keys('C:\\Users\\oliverchan\\Desktop\\uploadFiles\\uplaod.txt')

print(upload.get_attribute('value'))

'''
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
upload.send_keys('d:\\test1.png')  # send_keys
print(upload.get_attribute('value'))  # check value
'''

sleep(5)
driver.quit()