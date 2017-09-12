# -*- coding: utf-8 -*-

#test 1
l = list(map(lambda x: x * x, [1,2,3,4,5,6]))
print(l)

#test 2
f = lambda x: x * x
print(f)

print(f(5))

#test 3
def build(x, y):
	return lambda: x * x + y * y

print(build(1,2)())