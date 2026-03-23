# https://www.codewars.com/kata/65013fc50038a68939098dcf/train/python

# Passed

def party_people(lst):
    sorted_arr = sorted(lst)
    for _ in range(len(sorted_arr)):
        if len(sorted_arr) >= sorted_arr[-1]:
            break
            
        sorted_arr.pop()
            
    remaining_people_count = len(sorted_arr)
    return remaining_people_count

output = party_people([0, 2, 3, 5, 6, 6, 6, 7, 11, 12, 13, 14, 16, 19, 20])
print(output)