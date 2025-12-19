# https://www.codewars.com/kata/5a9e86705ee396d6be000091/train/python

# Passed

def check_three_and_two(array):
    count_dict = {}
    for char in array:
        if char not in count_dict:
            count_dict[char] = 0
        
        count_dict[char] += 1

    is_three_and_two = set(count_dict.values()) == {2, 3}
    return is_three_and_two

output = check_three_and_two(["a", "a", "a", "b", "b"])
print(output)