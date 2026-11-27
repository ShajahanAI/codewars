# https://www.codewars.com/kata/5e5acfe31b1c240012717a78/train/python

# Passed

def make_model_year(lst):
    result = dict()
    for elem in lst:
        if type(elem) == int:
            result['year'] = elem
        elif type(elem) == str:
            result['make'] = elem
        elif type(elem) == tuple:
            result['model'] = " ".join(elem).strip()
        elif type(elem) == bool:
            result['new'] = elem
    
    return result

output = make_model_year([1998, 'ford', ('mustang', 'gt'), False])
print(output)