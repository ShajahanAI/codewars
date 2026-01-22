# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

# Passed

def solution(text, ending):
    result = text.endswith(ending)
    return result

output = solution("samurai", "ai")
print(output)