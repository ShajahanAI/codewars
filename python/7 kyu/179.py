# https://www.codewars.com/kata/597d75744f4190857a00008d/train/python

# Passed

from collections import defaultdict

def paint_letterboxes(start, finish):
    frequency_dict = defaultdict(int)
    for num in range(start, finish + 1):
        for digit in str(num):
            frequency_dict[digit] += 1
                      
    frequency_list = [frequency_dict[str(digit)] for digit in range(10)]
    return frequency_list

output = paint_letterboxes(125, 132)
print(output)