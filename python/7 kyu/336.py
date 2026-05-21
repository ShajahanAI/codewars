# https://www.codewars.com/kata/6411b91a5e71b915d237332d/train/python

# Passed

def valid_parentheses(paren_str):
    balance = 0
    for char in paren_str:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -=1
            
        if balance < 0:
            break
            
    result = balance == 0
    return result

output = valid_parentheses("(()())()")
print(output)