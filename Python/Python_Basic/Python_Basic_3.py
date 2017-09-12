# -*- coding: utf-8 -*-

#test 1
classmates = ['Michael', 'Bob', 'Tracy']
s = len(classmates) - 1
print(classmates[s])

print(classmates[len(classmates) - 1])
print(classmates[-1])

#test 2
classmates.append('oliver')
print(classmates)

#test 3 
classmates.insert(1, 'yoeng')
print(classmates)

#test 4
classmates.pop()
print(classmates)

#test 5
classmates.pop(1) 
print(classmates)

#test 6
classmates[1] = 'yoen'
print(classmates)

#test 7
s = ['Apple', 1, True]
print(s)

#test 8 
mates = ['ava','life',['yoen','oliver'],'wright']
print(mates[2][1])

#test 9 
L = []
s = len(L)
print (s)

#test 10
t = ()
print (t)

#test 11
t = (1)
print (t)

#test 12
t = (1,)
print (t)

#test 13
t = ('a','b',['x','y'])
t[2][0] = 'q'
t[2][1] = 'w'
print (t)

#test 14
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print (L[0][0])
# 打印Python:
print (L[1][1])
# 打印Lisa:
print (L[2][2])

print (L[-1][-1])