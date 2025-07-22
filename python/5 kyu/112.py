# https://www.codewars.com/kata/5266fba01283974e720000fa/train/python

# Passed

def variance(numbers): 
    mean = sum(numbers)/len(numbers)
    square_of_differences = [(num - mean) ** 2 for num in numbers]
    variance = sum(square_of_differences)/len(numbers) 
    return variance

output = variance([8, 9, 10, 11, 12])
print(output)