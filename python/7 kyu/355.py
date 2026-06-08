# https://www.codewars.com/kata/557cffec8c3e8e55cc00010f/train/python

# Passed

def count_zeros(x):
    zeroes_count = 0
    for num in range(1, x + 1):
        if "0" in str(num):
            zeroes_count += str(num).count("0")
            
    return zeroes_count

output = count_zeros(200)
print(output)