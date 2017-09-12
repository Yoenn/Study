# -*- coding: utf-8 -*-

#test 1
L = []
for x in range(1, 11):
	L.append(x*x)

print(L)

#test 2
print([x*x for x in range(1, 11)])

print([x*x for x in range(1, 11) if x % 2 == 0])

#test 3
print([m+n for m in 'ABC' for n in 'XYZ'])

#test 4
import os
print([d for d in os.listdir('.')])
print([d for d in os.listdir()])

#test 5
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k,v in d.items():
	print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

L = [k + '=' + v for k, v in d.items()]
print(L)

#test 6
L = ['Yoeng', 'Oliver']
print([s.lower() for s in L])

#test 7
L1 = ['Yoeng', 'Oliver', 24, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str) ==1 ]
print([L2])