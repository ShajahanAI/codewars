# https://www.codewars.com/kata/583ebb9328a0c034490001ba/train/python 

# Passed

def duplicate_elements(m, n):
    m_elems = set(m)
    n_elems = set(n)
    
    result = bool(m_elems & n_elems)
    return result

output = duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9])
print(output)