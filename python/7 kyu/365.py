# https://www.codewars.com/kata/5704bf9b38428f1446000a9d/train/python

# Passed

from collections import Counter

def histogram(values: list[int], bin_width: int) -> list[int]:
    counter = Counter(values)
    max_value = max(values, default=-1)
    
    histogram_data = []
    for num in range(0, max_value + 1, bin_width):
        total_count = 0
        for val in range(num, num + bin_width):
            total_count += counter[val]
            
        histogram_data.append(total_count)
        
    return histogram_data

output = histogram([1, 1, 0, 1, 3, 2, 6], 2)
print(output)