# -*- coding:UTF-8 -*-

def f1(a, L=[]):
    """Variable default parameters."""
    L.append(a)
    return L

def f2(a, L=0):
    if L == 0:
        L = []
    L.append(a)
    return L

if __name__ == "__main__":
    print(f1(1))
    print(f1(2))
    print(f1(3))

    print(f2(1))   
    print(f2(2))   
    print(f2(3))   
