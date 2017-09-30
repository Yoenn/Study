# -*- coding: utf-8 -*-
#python 3.5 + selenium 3.5
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import ctime

from selenium.webdriver.support.select import Select
import os

driver = webdriver.Firefox(executable_path = "D:\Yoeng-\OneForAll\Selenium\Driver\geckodriver.exe")
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
#driver = webdriver.Chrome("D:\Yoeng-\OneForAll\Selenium\Driver\chromedriver.exe")

'''
first_url = 'https://www-u4.ufreight.com:8443/'
print("now access %s" %(first_url))
driver.get(first_url)

print(driver.title)
'''

'''
#print('设置窗口大小')

#全屏显示
driver.maximize_window() 

#参数数字为像素
driver.set_window_size(480,800)
'''

'''
#访问cas02
second_url = 'https://cas02.icil.net:8443/cas-server-webapp-3.5.0/login?service=https%3A%2F%2Fwww-u4.ufreight.com%3A8443%2Fc%2Fportal%2Flogin%3Fp_l_id%3D10183'
print("now access %s" %(second_url))
driver.get(second_url)
'''

'''
#返回login页面
print("back to %s" %(first_url))
driver.back()

#前进到cas02
print("forward to %s" %(second_url))
driver.forward()

#刷新页面
print("refersh page %s" %(second_url))
driver.refresh()
'''

'''
#点击和输入
driver.find_element_by_id("username").send_keys("oliverchan")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("oliverchan")
driver.find_element_by_id("password").send_keys("OliverChan7")
driver.find_element_by_name("submit").click()
print("login successfully")
'''

'''
#获取输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

#返回元素的属性值
attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

#返回元素的结果是否可见
result = driver.find_element_by_id('kw').is_displayed()
print(result)

#返回底部备案信息

#改变标准的输出码（使用cmd输出）
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

text = driver.find_element_by_id('cp').text
print(text)
'''

'''
#鼠标悬停操作
above = driver.find_element_by_id('_145_mySites')
ActionChains(driver).move_to_element(above).perform()

#鼠标双击操作
click = driver.find_element_by_id('aui_3_4_0_1_451')
ActionChains(driver).double_click(click).perform()
'''

'''
#输入框输入内容
driver.find_element_by_id('kw').send_keys('seleniumm')

#输入空格键 + '教程'
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys('教程')

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

# 通过回车键来代替单击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
'''

'''
#设置断言
print('Before Search')

#打印当前页面title
title = driver.title
print(title)

#打印当前页面URL
now_url = driver.current_url
print(now_url)

driver.find_element_by_id('kw').send_keys('seleniumm')
driver.find_element_by_id('su').send_keys(Keys.ENTER)
sleep(1)	#推迟调用线程运行

print('After Search')

#打印当前页面title
title = driver.title
print(title)

#打印当前页面URL
now_url = driver.current_url
print(now_url)

#获取结果数目
user = driver.find_element_by_class_name('nums').text
print(user)
'''

'''
#显示等待
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'kw2')))
element.send_keys('selenium')
'''

'''
#隐式等待
driver.implicitly_wait(10)

try:
	print(ctime())
	driver.find_element_by_id('kw2').send_keys('selenium')
except NoSuchElementException as e:
	print(e)
finally:
	print(ctime())
'''

'''
#定位一组元素
driver.find_element_by_id('kw').send_keys('seleniumm')
driver.find_element_by_id('su').send_keys(Keys.ENTER)
sleep(1)

texts = driver.find_elements_by_xpath('//div/h3/a')

for t in texts:
	print(t.text)
'''

'''
#多表单切换
driver.get('http://www.126.com')

driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('username')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_id('dologin').click()

#跳回到最外层页面
driver.switch_to.default_content()
driver.find_element_by_name('email').clear()
'''

#多窗口切换
#尝试多次定位元素
'''
search_window = driver.current_window_handle
print(search_window)

driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[7]').click()

driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div/div/div/div/div/div[1]/form/p[9]/a[1]').click()

#driver.find_element_by_link_text("立即注册").click()
sleep(5)

#获取当前所有打开窗口的句柄
all_handles = driver.window_handles
print(isinstance(all_handles,(int,list)))

#进入搜索页面
driver.switch_to.window(search_window)
sleep(5)

#进入注册窗口
for handle in all_handles:
	print(handle)
	if handle != search_window:
		print(handle)
		driver.switch_to.window(handle)
		print('now register window')
		sleep(2)
'''

'''
#警告框处理
#link = driver.find_element_by_link_text('设置')
link = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[8]')

ActionChains(driver).move_to_element(link).perform()

driver.find_element_by_link_text('搜索设置').click()

#选择下拉框的内容
sel = driver.find_element_by_xpath('/html/body/div[2]/div[7]/div/div/div/div[1]/form/div/table/tbody/tr[3]/td[2]/select')
Select(sel).select_by_value('50')
sleep(2)

driver.find_element_by_class_name('prefpanelgo').click()
sleep(2)

driver.switch_to.alert.accept()
'''

#上传文件
'''
file_path = 'file:///C:/Users/oliverchan/Desktop/upload.html'
driver.get(file_path)

uplaod = driver.find_element_by_name('file')
upload.send_keys('C:\\Users\\oliverchan\\Desktop\\uplaod.txt')

print(upload.get_attribute('value'))
'''

'''
driver.find_element_by_class_name('soutu-btn').click()

upload = driver.find_element_by_class_name('upload-pic')
upload.send_keys('C:\\Users\\oliverchan\\Desktop\\uplaod.png')
print(upload.get_attribute('value'))
'''

'''
#使用AutoIt识别上传
driver.find_element_by_class_name('soutu-btn').click()
driver.find_element_by_class_name('upload-pic').click()

#调用AutoIt的脚本
os.system('C:\\Users\\oliverchan\\Desktop\\script.exe')
'''

'''
#操作cookie
cookies = driver.get_cookies()
print(cookies)

driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbbbb'})

for cookie in driver.get_cookies():
	print('%s -> %s' %(cookie['name'], cookie['value']))
'''

'''
#调用JavaScript
driver.set_window_size(500,500)

driver.find_element_by_id('kw').send_keys('selenium')
#driver.find_element_by_id('su').click()
sleep(2)

#通过js设置浏览器窗口的滚动条位置
js = 'window.scrollTo(100,450);'
driver.execute_script(js)
'''

'''
#截图
sleep(2)
driver.get_screenshot_as_file('D:\\baidu.png')
'''

#关闭单个窗口

driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[7]').click()

driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div/div/div/div/div/div[1]/form/p[9]/a[1]').click()

sleep(5)
driver.close()

'''
sleep(5)
driver.quit()
'''