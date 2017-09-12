#-*- coding: utf-8 -*-
#test 1
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

print(next(g))

#test 2
g = (x * x for x in range(10))
for n in g:
	print(n)

#test 3
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

fib(6)

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

print(fib(6))

for n in fib(6):
	print(n)

#test 4
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return values:', e.value)
		break

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 3
	print('step 3')
	yield(5)

o = odd()
print(next(o))

print(next(o))