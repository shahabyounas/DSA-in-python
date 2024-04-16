import ctypes
from time import time

class DynamicArray:
    
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1
    
    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n -1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
            raise ValueError('value not found')
    
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    def _make_array(self, c):
        return (c * ctypes.py_object)()
    
arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
print(arr)
arr.insert(3, 433)



def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n

# print(compute_average(1000000))
        