# https://www.codewars.com/kata/56b4bae128644b5613000037/train/python

# Passed

def repeat_sum(l):
    num_to_arr_occurence_count_dict = dict()
    for arr in l:
        seen = set()
        for num in arr:
            if num in seen:
                continue
                
            seen.add(num)
            if num not in num_to_arr_occurence_count_dict:
                num_to_arr_occurence_count_dict[num] = 0
                
            num_to_arr_occurence_count_dict[num] += 1
    
    result = 0
    for num, arr_occurence_count in num_to_arr_occurence_count_dict.items():
        if arr_occurence_count > 1:
            result += num
            
    return result

output = repeat_sum([[1,2,3], [2,8,9], [7,123,8]])
print(output)