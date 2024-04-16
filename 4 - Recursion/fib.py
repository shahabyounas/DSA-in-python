"""Fibonacci series using recursion"""

def fib(n):
    if n == 0:
        return 1
    else:
        return n * fib(n - 1)
    
def bad_fib(n):
    list.append(n)
    if n <= 1:
        return n
    else: 
        return bad_fib(n - 2) + bad_fib(n - 1)

def good_fib(n):
    
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fib(n - 1)
        return (a+b, b)



