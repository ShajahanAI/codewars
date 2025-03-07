# https://www.codewars.com/kata/588854201361435f5e0000bd/train/python

# Passed

def array_conversion(arr):
    iter = 0
    while len(arr) != 1:
        iter += 1
        batches = []
        for idx in range(0, len(arr), 2):
            batches.append(arr[idx:idx + 2])
        
        if iter % 2 == 0:
            # even iteration (product of batches)
            arr = [batch[0] * batch[1] if len(batch) == 2 else batch[0] for batch in batches]
        else:
            # odd iteration (sum of batches)
            arr = [sum(batch) for batch in batches]
            
    return arr[0]

output = array_conversion([1, 2, 3, 4, 5, 6])
print(output)