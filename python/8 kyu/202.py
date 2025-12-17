# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

# Passed

def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return arr
    
    count_of_positives = 0
    sum_of_negatives = 0
    for num in arr:
        if num > 0:
            count_of_positives += 1
        else:
            sum_of_negatives += num
            
    result = [count_of_positives, sum_of_negatives]
    return result

output = count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
print(output)