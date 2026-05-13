# https://www.codewars.com/kata/5aa20a964a6b34417c00008d/train/python

# Passed

def find_page_number(pages):
    max_page = max(pages)
    pages_in_order = list(range(1, max_page + 1))
    result = []
    idx = 0
    for page_num in pages:
        if page_num != pages_in_order[idx]:
            result.append(page_num)
        else:
            idx += 1
            
    return result

output = find_page_number([1,2,10,3,4,5,8,6,7])
print(output)