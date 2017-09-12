#-*- coding:utf-8 -*-

#test 1
d = {'Yoeng':90,'justin':80,'oliver':70}
print (d['Yoeng'])

#test 2
d['oliver'] = 100
print (d['oliver'])

#test 3
a = 'Tom' in d
print (a)

#test 4
b = d.get('tom')
c = d.get('tom',-1)
print(b,c)

#test 5
d.pop('justin')
print (d)

#test 6
#key = [1,2,3]
#d[key] = 'a list'

#test 7
s = set([2,1,3])
print(s)

#test 8
s = set([1,2,3,4,1,2,3])
print(s)

#test 9
s.add(5)
print(s)
s.add(5)
print(s)

#test 10
s.remove(5)
print(s)

#test 11
a = 'abc'
b = a.replace('a','A')
print (a)
print (b)

#test 12
t = (1,2,3)
d = {t:10,'yoen':90}
print (d)

#t = (1, [2,3])
#d = {t:10,'yoen':90}
#print(s)

#test 13
t = (1,2,3)
s = set(t)
print (d)

t = (1, [2,3])
s = set(t)
print(s)