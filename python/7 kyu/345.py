# https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python

# Passed

def easyline(n):
    def get_coefficients(n, memo=dict()):
        if n in memo:
            return memo[n]

        if n == 0:
            return [1]
        
        result = [1] + get_coefficients(n - 1) + [1]
        coefficients = []
        for idx in range(1, len(result) - 2):
            coefficient = result[idx] + result[idx + 1]
            coefficients.append(coefficient)
        
        coefficients = [1] + coefficients + [1] 
        memo[n] = coefficients
        
        return coefficients
    
    coefficients = get_coefficients(n)
    result = sum(coefficient ** 2 for coefficient in coefficients)
    return result

output = easyline(13)
print(output)