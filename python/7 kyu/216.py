# https://www.codewars.com/kata/58ac59d21c9e1d7dc5000150/train/python

# Passed

import math

def make_parts(arr, chunk_size):
    batches = []
    for batch_num in range(1, math.ceil(len(arr) / chunk_size) + 1):
        start_idx = chunk_size * (batch_num - 1) 
        end_idx = chunk_size * batch_num
        batch = arr[start_idx:end_idx]
        
        batches.append(batch)
        
    return batches

output = make_parts([1,2,3,4,5], 2)
print(output)