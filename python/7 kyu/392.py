# https://www.codewars.com/kata/679bdbe30a5faf7bbf634e0f/train/python

# Passed

def naughty_number(arr):
    def contains_number(arr):
        arr_contains_number = False
        for elem in arr:
            if type(elem) == list:
                return contains_number(elem)
            elif type(elem) == int:
                arr_contains_number = True
                break

        return arr_contains_number

    for idx, elem in enumerate(arr):
        arr_contains_number = contains_number(elem)
        if arr_contains_number:
            return idx

        
output = naughty_number([[[]], [[[[[]]]]], [] , [[[[[[[[[]]]]]]]]], [[[]]], [[[[31]]]], [[]], []])
print(output)