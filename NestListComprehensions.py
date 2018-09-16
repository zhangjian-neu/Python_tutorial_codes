# -*- coding: UTF-8 -*-

matrix = [[col + row*4 + 1 for col in range(4) ] for row in range(3)]
print('matrix', matrix)

transposed = [[ row[i] for row in matrix] for i in range(4)]
print('transposed', transposed)

trans2 = list(zip(*matrix))
# * decompose the matrix into three lists.
# zip receives some iterable objects and return a zip iterable objects.
print(trans2)
