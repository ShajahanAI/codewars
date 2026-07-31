# https://www.codewars.com/kata/5729c30961cecadc4f001878/train/python

# Passed

def unite_unique(*args):
    result = []
    seen = set()
    for arr in args:
        for num in arr:
            if num not in seen:
                seen.add(num)
                result.append(num)
    
    return result

output = unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1])
print(output)