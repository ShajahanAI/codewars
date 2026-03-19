# https://www.codewars.com/kata/55f3facb78a9fd5b26000036/train/python

# Passed

def check_root(strng):
    numbers = strng.split(',')
    if len(numbers) != 4 or any(not num.lstrip("-").isdigit() for num in numbers):
        return "incorrect input"
    
    # checking if consecutive
    numbers = [int(num) for num in numbers]
    first_num = numbers[0]
    for idx in range(len(numbers)):
        if first_num + idx != numbers[idx]:
            return "not consecutive"
    
    perfect_square = numbers[0] * numbers[1] * numbers[2] * numbers[3] + 1
    square_root = int(perfect_square ** 0.5)
    
    result = f"{perfect_square}, {square_root}"
    return result

output = check_root('1015,1016,1017,1018')
print(output)