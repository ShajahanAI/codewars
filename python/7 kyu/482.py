# https://www.codewars.com/kata/52829c5fe08baf7edc00122b/train/python

# Passed

def number_of_occurrences(element, sample):
    result = sum(int(item == element) for item in sample)
    return result

output = number_of_occurrences(2, [0, 1, 2, 2, 3])
print(output)