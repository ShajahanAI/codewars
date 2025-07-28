# https://www.codewars.com/kata/58b972cae826b960a300003e/train/python

# Passed

def missing(nums, s):
    joined_code = "".join(s.split())
    deciphered_code = ""
    nums.sort()
    for idx in nums:
        if idx >= len(joined_code):
            return "No mission today"

        deciphered_code += joined_code[idx]
    
    deciphered_code = deciphered_code.lower()
    return deciphered_code
         
output = missing([29, 31, 8], "The quick brown fox jumps over the lazy dog")
print(output)