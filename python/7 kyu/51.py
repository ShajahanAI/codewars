# https://www.codewars.com/kata/559f44187fa851efad000087/train/python

# Passed

def seven_ate9(str_):
    result = str_.replace("797", "77")
    while result != result.replace("797", "77"):
        result = result.replace("797", "77")
        
    return result

output = seven_ate9("7979977732412979724979741")
print(output)