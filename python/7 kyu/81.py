# https://www.codewars.com/kata/525f039017c7cd0e1a000a26/train/python

# Passed

def palindrome_chain_length(n):
    is_number_palindrome = lambda num: str(num) == str(num)[::-1]
    steps = 0
    while not is_number_palindrome(n):
        n += int(str(n)[::-1])
        steps += 1

    return steps

output = palindrome_chain_length(87)
print(output)