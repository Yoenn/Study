#-*- coding: utf-8 -*-

#test1
print(int('12345'))

print(int('12345', base = 8))

print(int('12345', 16))

#test2
def int2(x, base = 2):
	return int(x, base)

print(int2('10000000'))

#test3
import functools
int3 = functools.partial(int, base = 2)
print(int3('10000000'))

#test4
max2 = functools.partial(max, 10)

print(max2(5, 6, 7))