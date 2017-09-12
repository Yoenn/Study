#-*- coding: utf-8 -*-
#test 1
def now():
	print('2015-3-25')

f = now
now()
f()

#test 2
print(now.__name__)

print(f.__name__)

#test 3
def log(func):
	def wrapper(*args, **kw):
		print('call %s:' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2015-3-25')

now()

#test 4
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('excute')
def now():
	print('2015-3-25')

now()