#-*- coding: utf-8 -*-
#test 1
from collections import Iterable
print(isinstance([],Iterable))

#test 2
from collections import Iterator
print(isinstance([],Iterator))

print(isinstance((x for x in range(10)),Iterator))

#test 3
print(isinstance(iter([]),Iterator))