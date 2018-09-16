# -*- codeing: UTF-8 -*-

def fib(n):
    """Generate Fib seriers < n."""
    a,b = 0,1
    while a<n:
        print(a)
        a, b = b, a+b
    print()

if __name__ == "__main__":
    fib(2000)

    
