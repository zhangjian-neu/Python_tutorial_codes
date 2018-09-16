# -*- coding: UTF-8 -*-

d = {'a':1, 'b':2}
print(d['b'])

del d['a']
print('del', d)

d['c'] = 3
print('add', d)

print('key list:', list(d.keys()))
print('key sort:', sorted(d.keys()))

print('create dict by key-value pairs:', dict([('a', 1), ('d', 4)]))
print('create dict by dict comprehensions:', {x: x**2 for x in range(5)})
print('create dict by key function parameters', dict( a = 1, d = 4))      
