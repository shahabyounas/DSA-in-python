from time import time

start_time = time()

result = []
for k in range(1, 10000):
    result.append(k)
    
end_time = time()

elapsed = end_time - start_time

print(elapsed)