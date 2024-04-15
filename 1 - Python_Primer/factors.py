from credit_card import CreditCard
from math import sqrt, pi

def factors(n):
    results = []
    for k in range(1, n + 1):
        if n % k == 0:
            results.append(k)
        
    return results

def factors_comp(n):
    return [k for k in range(1, n + 1) if n%k == 0]


def factors_with_g(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k

def factors_with_gg(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        future = a + b
        a = b
        b = future
        
def fib():
    a,b = 0, 1
    while True:
        yield a
        a, b = b, a + b


num = int(input())

for factor in factors_with_gg(num):
    print(factor)

#condition
result = factors(num if num >= 0 else -num)


def squares(n):
    result = []
    for k in range(1, n + 1):
        result.append(k * k)
    return result

def squares_com(n):
    return [k*k for k in range(1, n + 1)]



def isEven(n):
    return n%2 == 0

obj = {
    'k': [k for k in range(1, 100) if isEven(k)] 
}


large_abs = max(-34,-300, key=abs)
cache = vars().values()

# for c in cache.items():
print(sqrt(232))