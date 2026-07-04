# https://www.codewars.com/kata/6a2deeb1a8b6a4b0a80430af/train/python

# Passed

def do_they_agree(alice, bob):
    smaller_list, larger_list = sorted([alice, bob], key=len)
    num_to_larger_list_idx_dict = {
        num: idx for idx, num in enumerate(larger_list)
    }
    
    larger_set = set(larger_list)
    latest_idx = 0
    
    result = True
    for num in smaller_list:
        if num in larger_set:
            if latest_idx > num_to_larger_list_idx_dict[num]:
                result = False
                break
            
            latest_idx = num_to_larger_list_idx_dict[num]
            
    return result

output = do_they_agree((1, 2, 3, 6), (1, 2, 4))
print(output)