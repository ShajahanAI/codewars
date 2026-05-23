# https://www.codewars.com/kata/5aa39ba75084d7cf45000008/train/python

# Passed

def solve(n, memo=dict()):
    if (n in memo):
        result = memo[n]
        return result
    
    if (n == 0):
        return "0"
    elif (n == 1):
        return "01"
    
    result = solve(n - 1) + solve(n - 2)
    memo[n] = result
    return result

output = solve(3)
print(output)