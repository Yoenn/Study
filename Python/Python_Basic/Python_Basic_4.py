# -*- coding: utf-8 -*-
#test 1 
age = 20;
if age>6:
	print("teenager")
elif age>18:
	print('adult')
else:
	print('kid')

#test 2
s = input("输入一个数：")
birth = int(s)
if birth <2000:
	print('00前')
else:
	print('00后')

#test 3
# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = weight/(height*height)
print(bmi)
if bmi < 18.5:
	print('你的体重过轻')
elif bmi > 18.5 and bmi <= 25:
	print('你的体重正常')
elif bmi > 25 and bmi <= 28:
	print('你的体重过重')
elif bmi > 28 and bmi <= 32:
	print('你的体重肥胖')
else:
    print('你的体重严重肥胖')