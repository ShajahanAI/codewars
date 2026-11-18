# https://www.codewars.com/kata/5a7893ef0025e9eb50000013/train/python

# Passed

def max_gap(numbers):
    sorted_numbers = sorted(numbers)
    result = None
    for idx in range(len(sorted_numbers)):
        if idx == len(sorted_numbers) - 1:
            break
            
        gap = abs(sorted_numbers[idx] - sorted_numbers[idx + 1])
        if result is None:
            result = gap
        else:
            result = result if gap <= result else gap
    
    return result

output = max_gap([24, 299, 131, 14, 26, 25])
print(output)