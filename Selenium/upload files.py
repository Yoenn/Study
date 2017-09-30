#-*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path = "D:\Yoeng-\OneForAll\Selenium\Driver\geckodriver.exe")

#driver = webdriver.Chrome("D:\Yoeng-\OneForAll\Selenium\Driver\chromedriver.exe")

driver.implicitly_wait(10)

driver.get('https://www-u4.ufreight.com:8443/')

#click sign in, access cas02
driver.find_element_by_id("sign-in").click()

#login
driver.find_element_by_id("username").send_keys("oliverchan")
driver.find_element_by_id("password").send_keys("#")
driver.find_element_by_name("submit").click()
print("login successfully")
sleep(2)

#show Go to list
GoTo = driver.find_element_by_id('_145_mySites')
ActionChains(driver).move_to_element(GoTo).perform()
print('show go-to')
sleep(2)

#click Ufreight Private
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/ul/li[5]').click()

print('ufreight private')

#click Documents
driver.find_element_by_id('aui_3_4_0_1_427').click()

#Customers Repository
driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div/div/div/div/section/div/div/div/div/div[1]/div/div[2]/div/form/div[1]/div[1]/div/div/table/tbody/tr[5]/td[2]/span/a/span').click()

#click Ufreight
driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div/div/div/div/section/div/div/div/div/div[1]/div/div[2]/div/form/div[1]/div/div[1]/div/div/table/tbody/tr[3]/td[2]/span/a/span').click()

#click Lazada
driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div/div/div/div/section/div/div/div/div/div[1]/div/div[2]/div/form/div[1]/div/div[1]/div/div/table/tbody/tr[6]/td[2]/span/a/span').click()

#click booking document
driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div/div/div/div/section/div/div/div/div/div[1]/div/div[2]/div/form/div[1]/div[1]/div/div/table/tbody/tr[3]/td[2]/span/a/span').click()
sleep(5)

#click ADD
driver.find_element_by_xpath('html/body/div[6]/div/div[2]/div/div/div/div/div/section/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[2]/span[5]/span/span/ul/li/strong/a/span').click()
print('add')

#click LAZADA booking document
driver.find_element_by_xpath('html/body/div[1]/div/div/div/ul/li[2]/a').click()
sleep(2)

#upload file
upload = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div/section/div/div/div/form/fieldset/div/span[1]/span/span/input')
upload.send_keys('C:\\Users\\oliverchan\\Desktop\\SZ_SEKO_Manifest_201709221810.xlsx')
pritn(upload.get_attribute('value'))

sleep(5)
#driver.quit()