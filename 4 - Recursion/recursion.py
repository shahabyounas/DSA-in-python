"""
1 - Inefficient use of recursion
2 - Maximum recursive depth, if base case is not met, there for each 
    recursion should progress towards base case, the default recursion limit is = 1000 in python
    The infinite recursion can swamp computing resources, CPU, because each successive call creates
    activation record requiring additional memory.
"""

# import sys
# old = sys.getrecursionlimit()
# sys.setrecursionlimit(10000)


def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n -1]

numbers = [4,3,6,2,8]
# print(linear_sum(numbers, len(numbers)))


def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop -1], S[start]
        reverse(S, start + 1, stop -1)
    return S

def reverse_loop(S):
    start = 0
    end = len(S) - 1
    while(start < end):
        S[start], S[end] = S[end], S[start]
        start += 1
        end -= 1
    return S

def pow(x, n):
    if n == 0:
        return 1
    else:
        return x * pow(x, n - 1)

def pow_op(x, n):
    if n == 0:
        return 1
    else:
        partial = pow(x, x // 2)
        result  = partial * partial
        if n % 2 == 1:
            result *= x
        return result

def binary_sum(S, start, stop):
    
    if start > stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
        
    
# print(reverse(numbers, 0, len(numbers)))
print(reverse_loop(numbers))

def numbers(n):
    if n == 1:
        return 1
    print(n)
    return n + numbers(n - 1)
