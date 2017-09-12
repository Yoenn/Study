# -*- coding: utf-8 -*-

#test 1
d = {'a' : 1,'b' : 2, 'c' : 3}
for key in d:
	print(key)

for value in d.values():
	print(value)

for k,v in d.items():
	print(k,v)

#test 2
for ch in 'ABC':
	print(ch)

#test 3
from collections import Iterable
print(isinstance('abc', Iterable))

print(isinstance([1, 2, 3], Iterable))

print(isinstance(123, Iterable))

#test 4
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

#test 5
for x, y in [(1,1), (2,4), (3,9)]:
	print(x,y)

for z in [(1,1), (2,4), (3,9)]:
	print(z)