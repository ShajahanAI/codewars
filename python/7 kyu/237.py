# https://www.codewars.com/kata/58f6f87a55d759439b000073/train/python

# Passed

def negation_value(s: str, val) -> bool:
    boolean_val = bool(val)
    for _ in s:
        boolean_val = not(boolean_val)
        
    return boolean_val
        
output = negation_value("!!!", [])
print(output)