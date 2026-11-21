# https://www.codewars.com/kata/5a21e090f28b824def00013c/train/python

# Passed

def switch_dict(dic):
    result = dict()
    for key, val in dic.items():
        if val not in result:
            result[val] = list()
        
        result[val].append(key)
    
    return result

output = switch_dict(
    {
        'Ice': 'Cream',
        'Age': '21',
        'Light': 'Cream',
        'Double': 'Cream'
    }
)
print(output)