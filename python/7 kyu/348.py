# https://www.codewars.com/kata/580a4001d6df740d61000301/train/python

# Passed

def complete_series(seq): 
    val_to_count_dict = dict()
    for val in seq:
        if val not in val_to_count_dict:
            val_to_count_dict[val] = 0
            
        val_to_count_dict[val] += 1
        if val_to_count_dict[val] > 1:
            result = [0]
            break
    else:
        result = list(range(0, max(seq) + 1))
            
    return result

output = complete_series([1, 4, 6])
print(output)