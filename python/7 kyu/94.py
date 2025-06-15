# https://www.codewars.com/kata/5a092d9e46d843b9db000064/train/python

# Passed

def solve(arr):
    all_numbers = set(arr)
    for num in all_numbers:
        if -num not in all_numbers:
            return num
        
output = solve([-110, 110, -38, -38, -62, 62, -38, -38, -38])
print(output)