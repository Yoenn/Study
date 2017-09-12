#test 1
a = 100
print(a)

#test 2
print('100+200=',100+200)

#test 3
#name = input('please input your name: ')
name = 'yoen';
print('Hello,',name)

#test 4
print('1024 * 768 =',1024*768)

#test 5
print('I\'m \nok!')

#test 6
print(r"\\\t\\\\\'")
print(r'\\\\tt\\\'')

#test 7
print('''
123
456
789''')

#test 8
print(r'''
123
456
\\\\t\\\\
''')

#test 9
print(r'\\\t\\')

#test 10
print('''
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \\'Adam\\''
s3 = r'Hello, "Bart"'
s4 = r\'''Hello,
Lisa!\'''
	''')

#test 11 (it is a not ok way. it is stop in the line 57, after s4 = r.)
print(r'''
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
	''')
