# https://www.codewars.com/kata/5cc80fbe701f0d001136e5eb/train/python

# Passed

def stem_and_leaf(data):
    result = dict()
    for num in data:
        num_str = ("0" if len(str(num)) == 1 else str()) + str(num)
        stem = int(num_str[0])
        if stem not in result:
            result[stem] = list()
        
        for leaf in num_str[1:]:
            result[stem].append(int(leaf))
            
    for stem in result:
        result[stem].sort()
        
    return result

output = stem_and_leaf([11, 35, 14, 9, 39, 23, 35])
print(output)