# https://www.codewars.com/kata/52f5424d0531259cfc000d04/train/python

# Passed

def sort_by_bit(seq):
    print(seq)
    seq = [idx for idx in seq if idx < 32]
    binary_num_arr = ["0"] * (max(seq) + 1) if len(seq) != 0 else ["0"] 
    for idx in seq:
        binary_num_arr[idx] = "1"
        
    binary_num_arr = binary_num_arr[::-1]
    binary_num = "".join(binary_num_arr)
    result = int(binary_num, 2)
    return result

output = sort_by_bit([1, 0])
print(output)