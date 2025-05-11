# https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python

# Passed

from string import ascii_lowercase

def change(st):
    alphabets = list(ascii_lowercase)
    res = str()
    for alphabet in alphabets:
        if alphabet in st.lower():
            res += "1"
        else:
            res += "0"
    
    return res            

output = change('Abc e  $$  z')
print(output)