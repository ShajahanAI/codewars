# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python

# Passed

def even_last(numbers): 
    result = 0
    last_idx = len(numbers) - 1
    for idx, num in enumerate(numbers):
        if idx % 2 == 0:
            result += num

        if idx == last_idx:
            result *= num

    return result

output = even_last([2, 3, 4, 5])
print(output)