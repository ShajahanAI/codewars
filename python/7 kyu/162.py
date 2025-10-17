# https://www.codewars.com/kata/5a63948acadebff56f000018/train/python

# Passed

def max_product(lst, n_largest_elements):
    lst.sort(reverse=True)
    result = 1
    for idx in range(n_largest_elements):
        result *= lst[idx]
        
    return result

output = max_product([10,2,3,8,1,10,4], 5)
print(output)