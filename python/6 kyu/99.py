# https://www.codewars.com/kata/59590976838112bfea0000fa/train/python

# Passed

def beggars(values, n):
    result = []
    for beggar_idx in range(n):
        beggar_collection = 0
        while beggar_idx < len(values):
            collection = values[beggar_idx]
            beggar_collection += collection
            beggar_idx += n
        result.append(beggar_collection)

    return result

output = beggars([1,2,3,4,5], 3)
print(output)