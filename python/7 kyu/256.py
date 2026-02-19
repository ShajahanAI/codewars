# https://www.codewars.com/kata/515ceaebcc1dde8870000001/train/python

# Passed

def solution(items, index, default_value):
    try:
        result = items[index]
    except Exception as e:
        result = default_value
        
    return result

output = solution([None, None], 0, 'a')
print(output)