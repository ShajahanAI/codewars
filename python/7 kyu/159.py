# https://www.codewars.com/kata/58daa7617332e59593000006/train/python

# Passed

def find_longest(arr):
    longest_num = str()
    for num in arr:
        if len(str(num)) > len(str(longest_num)):
            longest_num = num
            
    return longest_num

output = find_longest([9000, 8, 800])
print(output)