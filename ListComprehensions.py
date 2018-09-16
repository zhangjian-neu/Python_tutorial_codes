# -*- coding: UTF-8 -*-

from math import pi


squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)  

xy = [(x, y) for x in range(1,3) for y in range(1,3) if x != y]
print(xy)

roundPi = [str(round(pi, i)) for i in range(1,6)]
print('round(pi)', roundPi)

