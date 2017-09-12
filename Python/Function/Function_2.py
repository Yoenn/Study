# -*- coding: utf-8 -*-

#test 1
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad oprend type')
	if x>= 0:
		return x
	else:
		return -x

#test 2
import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

r = x, y = move (100,100,60, math.pi /6)
print (math.pi)
print (x,y)
print (r)

#test 3
import math

def quadatic(a,b,c):
	z = b * b - 4 * a* c
	if z >= 0:
		x = (- b + math.sqrt(z))/(2 * a)
		y = (- b - math.sqrt(z))/(2 * a)
		return x,y
	else:
		return '该方程无解'

print(quadatic(2,3,1))
print(quadatic(1,3,-4))
print(quadatic(1,1,4))