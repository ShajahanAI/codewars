# https://www.codewars.com/kata/546dba39fa8da224e8000467/train/python

# Passed

def run_length_encoding(s):
    count = 1
    result = []
    for idx in range(len(s)):
        if idx != len(s) - 1 and s[idx] == s[idx + 1]:
            count += 1
        else:
            result.append([count, s[idx]])
            count = 1
            
    return result

output = run_length_encoding("hello world!")
print(output)