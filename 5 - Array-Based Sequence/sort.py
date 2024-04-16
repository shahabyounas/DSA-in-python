def insertion_sort(A):
    
    for k in range(1, len(A)):
        cur = A[k]
        print("cur", A[k])
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j -1]
            j -= 1
        A[j] = cur
        print(A)
    return A

print(insertion_sort([34,4,5,2,4,5,3,6,1,100,1000]))