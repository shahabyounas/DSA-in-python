import sys

"""
    Operation               | Running Time   
    len(data)                 O(1)
    data[j]                   O(1)
    data.count(value)         O(N)
    data.index(value)         O(k + 1)
    val in data               O(k + 1)
    data1 == data1            O(k + 1)
    (!-, <, > , <=, >=)
    data[j:k]                 O(k - j + 1)
    data1 + data2             O(n1 + n2)
    c * data                  O(cn)
    
Operation Running Time
    data[j] = val                   O(1)
    data.append(value)              O(1)
    data.insert(k, value)           O(n - k+1)
    data.pop( )                     O(1)
    data.pop(k) or del data[k]      O(n - k)
    data.remove(value)              O(n)
    data1.extend(data2)             O(n2)
    data1 += data2  
    data.reverse( )                 O(n)
    data.sort( )                    O(nlog n)
"""

data = []

for k in range(10):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append("None" + str(k))
    


    
    
    
    