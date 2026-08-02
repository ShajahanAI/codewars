# https://www.codewars.com/kata/586efc2dcf7be0f217000619/train/python

# Passed

def reverse_slice(s):
    result = []
    string_to_append = ""
    for char in s:
        string_to_append += char
        result.append(string_to_append[::-1])
        
    result = result[::-1]
        
    return result

output = reverse_slice('abcde')
print(output)