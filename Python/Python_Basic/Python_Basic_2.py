# -*- coding: utf-8 -*-

#test 1
a = ord('A')
print (a)

b = chr(25991)
print (b)

#test 2
C = b'ABC'.decode('utf-8')
print(C)

D = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(D)

E = 'ABC'.encode('ascii')
print(E)

#test 3
A = 'Hello, %s, you are %d years old' % ('Yoen', 22)
print(A)

'''(annotate this code for other training)
S = input("your name: ")
A = 'Hello, %s' % S
print(A)
'''

#tset 4
# -*- coding: utf-8 -*-
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('%.1f%%' % r)

#test 5
print('%02d,%.2d,%02f,%.2f' %(1,2,3,4))