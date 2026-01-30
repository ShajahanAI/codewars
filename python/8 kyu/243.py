# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python

# Passed

def same_case(a, b): 
    if a.isalpha() and b.isalpha():
        # both are letters
        if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
            return 1 # same case
        else:
            return 0 # not same case
    
    return -1

output = same_case('C', 'B')
print(output)