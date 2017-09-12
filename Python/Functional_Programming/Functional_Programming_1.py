#-*- coding: utf-8 -*-

#test 1
print(abs(-10))

f = abs

print(f(-20))

abs = 30

print(abs)

#test 2
def add(x, y, f):
	return f(x) + f(y)

print(add(-5, -6, f))