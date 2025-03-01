# https://www.codewars.com/kata/58520e8edeb17c711c00019b/train/python

# Passed

def merry_christmas(funcs):
    character_function_dict = {
        func(): func.__name__ for func in funcs
    }

    string_to_form = 'Merry Christmas!'
    return ','.join([character_function_dict[char] for char in string_to_form])

def func(name, value):
    f = lambda: value
    f.__name__ = name
    return f

funcs = [func(tup[0], tup[1]) for tup in  
           [('a',   'M'),
            ('b',   'e'),
            ('c',   'r'),
            ('d',   'y'),
            ('e',   'C'),
            ('f',   'h'),
            ('g',   'i'),
            ('h',   's'),
            ('i',   't'),
            ('j',   'm'),
            ('k',   'a'),
            ('l',   ' '),
            ('m',   '!'),]]

output = merry_christmas(funcs)
print(output)