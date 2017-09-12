#-*- coding: utf-8 -*-

#test1
def f(x):
	return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#test 2
from functools import reduce
def add(x, y):
	return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

#test 3
from functools import reduce
def fn(x, y):
	return x * 10 +y

reduce(fn, [1, 3, 5, 7, 9])

#test 4
def fn(x ,y):
	return x * 10 +y

def char2num(s):
	return {'1': 1, '3': 3, '5': 5, '7': 7, '9': 9}[s]

print(reduce(fn, map(char2num, '13579')))


#整理成一个函数
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'1': 1, '3': 3, '5': 5, '7': 7, '9': 9}[s]
	return reduce(fn, map(char2num, s))

print(str2int('1357'))

#进一步优化
def char2num(s):
	return {'1': 1, '3': 3, '5': 5, '7': 7, '9': 9}[s]

def str2int(s):
	return reduce(lambda x, y : x * 10 +y, map(char2num, s))

print(str2int('135'))


#test 5
def normalize(name):
	return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#test 6
def prod(L):
	def M(x, y):
		return x * y
	return reduce(M, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


#test 7
def str2float(s):
    # 找到小数点索引位置
    dotIndex = s.find('.')
    # 移除小数点
    s = s.replace('.', '')
    # 需要缩小的倍数
    dotTimes = len(s) - dotIndex

    return reduce(lambda x, y: x*10+y, map(int, s)) / pow(10, dotTimes)

print('str2float(\'123.456\') =', str2float('123.456'))
