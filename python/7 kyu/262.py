# https://www.codewars.com/kata/5af15a37de4c7f223e00012d/train/python

# Passed

def men_from_boys(arr):
    men_nums, boy_nums = [], []
    seen = set()
    for num in arr:
        if num in seen:
            continue
        
        if num % 2 == 0:
            men_nums.append(num)
        else:
            boy_nums.append(num)
            
        seen.add(num)
        
    men_nums.sort()
    boy_nums.sort(reverse=True)
    
    sorted_arr = men_nums + boy_nums
    return sorted_arr

output = men_from_boys([2,43,95,90,37])
print(output)