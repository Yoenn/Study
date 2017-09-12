#-*- coding: utf-8 -*-

#位置参数
#test 1
def power(x):
	return x*x

print(power(5))

#test 2
def power(x,n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print (power(5,3))

#默认参数
#test 1
def power3(x,n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power3(5,3))
print(power3(5))

#test 2
def enroll(name, gender, age = 6, city = 'Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

enroll('Yoen','M')

enroll('oliver','F',city = 'ShenZhen')

#test 3
def add_end(L=[]):
	L.append('END')
	return L

print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())

#test 4
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

print(add_end())
print(add_end())

#可变参数
#test 1
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print(calc([1,2,3]))
print(calc((1,2,3,5)))

#test 2
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n 
	return sum

print(calc(1,2))

nums = [1,2,3]
print(calc(*nums))

nums1 = (1,2,5)
print(calc(*nums1))

#关键字参数
#test 1
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

person('Yoen',24)

#test 2
person('Yoen',24,city='ShenZhen')

person('Yoen', 24, city = 'ShenZhen', job = 'Enginneer')

#test 3
extra = {'city':'ShenZhen', 'job':'Enginneer'}
person('Yoeng', 25, city = extra['city'], job = extra ['job'])

person('Yoeng', 25, **extra)

#命名关键字参数
#test 1
def person(name, age, *, city, job):
	print(name,age,city,job)

person('Jack',24, city = 'ShenZhen', job = 'Enginneer')

#test 2
def person(name, age, *args, city, job):
	print(name, age, args, city, job)


person('Yoen',14, 'Beijing', 'ShenZhen', city = 'Beijing', job = 'Enginneer')

#test 3
def person(name, age, *, city = 'ShenZhen', job):
	print(name, age, city, job)
	
person('Yoen', 24, job = 'Enginneer')

#参数组合
#test 1
def f1(a, b, c = 0, *args, **kw):
	print('a=', a, 'b=', b, 'c =', c, 'args =', args, 'kw = ', kw)

def f2(a, b, c =0, *, d, **kw):
	print('a=', a, 'b=', b, 'c =', c, 'd =', d, 'kw = ', kw)

print(f1(1, 2))
print(f1(1, 2, c=4))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x = 99))
print(f2(1, 2, d = 99, ext = None))

#test 2
args = (1, 2 , 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args,**kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args,**kw)