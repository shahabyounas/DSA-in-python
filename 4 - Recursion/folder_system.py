import os

def disk_usage(path):
    total = os.path.getsize(path)
    
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)
    
    print('{0: <5}'.format(total), path)
    return total


#Display all the file/s inside the given directory
print(disk_usage('/Users/Work/Desktop/projects/DSA-in-python/4 - Recursion'))

