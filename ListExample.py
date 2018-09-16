# -*- coding: UTF-8 -*-

L = []
x = 0

L.append(x)
print(L)

L1 = [1,2]
L.extend(L1)
print(L)

L.insert(0,5) 
print(L)    

L.remove(5)
print(L)    

L.pop(0)
print(L)

L.clear()
print(L)

L = ['a', 'b']
print('New list', L)

print('index', L.index('a'))

L.sort()
print('sort', L)

L.reverse()
print('reverse', L)
L2 = L1.copy()
print('Shallow copy', L2)
print('id(L)', id(L), 'id(L2)', id(L2))
#print(id(L2))

