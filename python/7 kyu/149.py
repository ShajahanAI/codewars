# https://www.codewars.com/kata/57f12b4d5f2f22651c00256d/train/python

# Passed

def array_info(x):
    array_length = len(x)
    if array_length == 0:
        return "Nothing in the array!"

    integers = 0
    floats = 0
    strings = 0
    whitespaces = 0
    for item in x:
        if type(item) == int:
            integers += 1
        elif type(item) == float:
            floats += 1
        elif type(item) == str:
            if len(item.strip()) == 0:
                whitespaces += 1
            else:
                strings += 1
    
    transform = lambda info: [info] if info != 0 else [None] 
    result = [transform(array_length), transform(integers), transform(floats), transform(strings), transform(whitespaces)]
    return result

output = array_info([1,2,3.33,4,5.01,'bass','kick',' '])
print(output)