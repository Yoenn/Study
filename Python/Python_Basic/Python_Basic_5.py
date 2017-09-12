# -*- coding: utf-8 -*-
#test 1
names = ['yoen','oliver','justin']
for name in names:
	print (name)

L = list(range(10))
print(L)

sum = 0
for x in range(101):
	sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

#test 2
for name in names:
	print('Hello,%s!'%name)

#test 3
n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n = n + 1
print('END')

#test 4
n = 0
while n < 10:
	n = n + 1
	if n % 2 ==0:
		continue
	print(n)