# https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3/train/python

# Passed

def calculate(strng):
    if "loses" in strng:
        operator = "subtraction"
    elif "gains" in strng:
        operator = "addition"
    
    lhs_rhs = [int(phrase) for phrase in strng.split(" ") if phrase.isdigit()]
    lhs, rhs = lhs_rhs
    
    result = lhs + rhs if operator == "addition" else lhs - rhs
    return result

output = calculate("Jerry has 34 apples and gains 6")
print(output)