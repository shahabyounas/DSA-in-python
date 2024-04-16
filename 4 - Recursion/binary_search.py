def binary_search(data, target, low, high):
    
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        
        if target == data[mid]:
            return True
        
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
        


data = [1,2,3,4,5,6,7,8,9,10]
target = 17
low = 0
high = len(data) - 1

# print(binary_search(data, target, low, high))




def b_search(data, target, low, high):
    
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return b_search(data, target, low, mid -1)
        else:
            return b_search(data, target, mid+1, high)
        

print(b_search(data, target, low, high))