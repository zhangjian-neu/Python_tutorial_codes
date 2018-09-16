# -*- coding: UTF-8 -*-

t = (3, (1, 6))
print('a tuple', t)

# t[0] = 5
# incorrect. 
# a tuple cannot be added by a element.

t = (3, (1, 6), [2, 4])
print('a tuple', t)     
t[2][0] = 5
print('the changed tuple', t)     

