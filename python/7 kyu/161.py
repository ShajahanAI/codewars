# https://www.codewars.com/kata/5a0366f12b651dbfa300000c/train/python

# Passed

def arbitrate(inp, n):
    if "1" not in inp:
        # no master is requesting access
        result = "0" * n
        return result
    
    idx = inp.index("1")
    result = ["0"] * n
    result[idx] = "1"
    result = "".join(result)
    
    return result

output = arbitrate("001000101", 9)
print(output)