# https://www.codewars.com/kata/6071ef9cbe6ec400228d9531/train/python

# Passed

def calculator(txt):
    get_first_and_second_term = lambda operator: (len(txt.split(operator)[0].strip()), len(txt.split(operator)[1].strip()))

    if "+" in txt:
        first_term, second_term = get_first_and_second_term("+")
        result = (first_term + second_term) * "."
    elif "-" in txt:
        first_term, second_term = get_first_and_second_term("-")
        result = (first_term - second_term) * "."
    elif "*" in txt:
        first_term, second_term = get_first_and_second_term("*")
        result = (first_term * second_term) * "."
    else:
        first_term, second_term = get_first_and_second_term("//")
        result = (first_term // second_term) * "."
        
    return result
        
output = calculator("..... + ...............")
print(output)