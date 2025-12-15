# https://www.codewars.com/kata/6113c2dc3069b1001b8fdd05/train/python

# Passed

def count_duplicates(name,age,height):
    seen = set()
    duplicates_counter = 0
    for n, a, h in zip(name, age, height):
        key = n + str(a) + str(h)
        if key in seen:
            duplicates_counter += 1
        else:
            seen.add(key)
            
    return duplicates_counter

output = count_duplicates(['John','Beth','Beth','Beth','Bill'], [37,23,23,23,46], [183,170,170,170,175])
print(output)