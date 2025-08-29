# https://www.codewars.com/kata/5a2d70a6f28b821ab4000004/train/python

# Passed

def largest_sum(s):
    numbers = [int(num) for num in s.split("0") if num]
    digit_sums = [0] # incase s is "0"
    for num in numbers:
        digits = [int(digit) for digit in str(num)]
        digit_sums.append(sum(digits))

    result = max(digit_sums)
    return result

output = largest_sum("72102450111111090")
print(output)