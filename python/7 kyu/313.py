# https://www.codewars.com/kata/5f77d62851f6bc0033616bd8/train/python

# Passed

def valid_spacing(s):
    split_terms = s.split(' ') if s else []
    result = all(term != '' for term in split_terms)
    return result

output = valid_spacing('Hello world')
print(output)