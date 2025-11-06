# https://www.codewars.com/kata/56459c0df289d97bd7000083/train/python

# Passed

def generator(_from, _to, _step):
    if _step == 0:
        return []
    
    if _from > _to:
        _step = -_step
        _to -= 2
        
    result = list(range(_from, _to + 1, _step))
    return result

output = generator(20, 10, 1)
print(output)