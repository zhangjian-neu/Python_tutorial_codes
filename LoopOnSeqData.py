# -*- coding: UTF-8 -*-

# for a dict, use items()
d = {'a':1, 'b':2}
for k, v in d.items():
    print(k, v)

# for a list or tuple, use enumerate()
l = [3, 5, 6]
for i, v in enumerate(l):
    print(i, v)

# loop two sequences, use zip()
questions = ['a', 'b']
answers = [1, 2]
for q,a in zip(questions, answers):
    print(q,a)

# loop in reversed order
questions = ['a', 'b']
for q in reversed(questions):
    print(q)

# loop in sorted order
answers = [3,7,1]
for a in sorted(answers):
    print(a)

# change the original seq, when loop, use slice
l = [1,2,3]
for i in l[:]:
    print(i)
    if i >= 2 :
        l.append(4)
print(l)        
