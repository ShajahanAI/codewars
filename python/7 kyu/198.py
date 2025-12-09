# https://www.codewars.com/kata/59dd2c38f703c4ae5e000014/train/python

# Passed

def solve(s:str) -> int:
    nums = []
    
    num = str()
    for idx, char in enumerate(s):
        if char.isdigit():
            num += char
        
        if num and (not char.isdigit() or idx == len(s) - 1):
            num = int(num)
            nums.append(num)
            num = str()
            
    largest_num = max(nums)
    return largest_num

output = solve('gh12cdy695m1')
print(output)