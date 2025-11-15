# https://www.codewars.com/kata/5a941f4e1a60f6e8a70025fe/train/python

# Passed

def odd_ball(arr):
    numbers_present = set()
    odd_indexes = []
    for idx, item in enumerate(arr):
        if type(item) == int:
            numbers_present.add(item)
        elif item == "odd":
            odd_indexes.append(idx)
            
    result = any(idx in numbers_present for idx in odd_indexes)
    return result

output = odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])
print(output)