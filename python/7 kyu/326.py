# https://www.codewars.com/kata/67a61fa0ed1d3932f2c39b66/train/python

# Passed

def sort_by_depth(arr):
    def get_depth(item):
        if len(item):
            return 1 + get_depth(item[0])
            
        return 0
    
    result = sorted(arr, key=get_depth)
    return result

output = sort_by_depth([ [[[[[]]]]], [[]], [], [[[]]], []])
print(output)