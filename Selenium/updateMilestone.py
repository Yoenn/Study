# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path = "D:\Yoeng-\OneForAll\Selenium\Driver\geckodriver.exe")
driver.implicitly_wait(10)

driver.get('https://www-u7.ufreight.com/UFL-ECommerce/')

driver.find_element_by_xpath('/html/body/div/div/nav[1]/section/ul/li[2]/a').click()

#cas02, login
driver.find_element_by_id("username").send_keys("oliverchan")
driver.find_element_by_id("password").send_keys("#")
driver.find_element_by_name("submit").click()
print("login successfully")



sleep(5)
driver.quit()