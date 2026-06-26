# https://www.codewars.com/kata/5b2117eea454c89d4400005f/train/python

# Passed

def leonardo_numbers(n, L0, L1, add) :
    result = []
    for iter_num in range(1, n + 1):
        if iter_num == 1:
            result.append(L0)
        elif iter_num == 2:
            result.append(L1)
        else:
            val = result[-1] + result[-2] + add
            result.append(val)
            
    return result

output = leonardo_numbers(5, 1, 1, 1)
print(output)