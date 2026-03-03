# https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python

# Passed

def div_con(x):
    int_total, string_total = 0, 0
    for elem in x:
        if type(elem) == str:
            string_total += int(elem)
        else:
            int_total += elem
            
    result = int_total - string_total
    return result

output = div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7])
print(output)