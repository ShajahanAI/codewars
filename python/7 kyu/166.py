# https://www.codewars.com/kata/5ce6cf94cb83dc0020da1929/train/python

# Passed

def uglify_word(s):
    flag = 1
    result = str()
    for letter in s:
        if letter.isalpha():
            if flag == 1:
                result += letter.upper()
            elif flag == 0:
                result += letter.lower()        
            
            flag = int(not flag)
        else:
            result += letter
            flag = 1
            
    return result
        
output = uglify_word("qwe123asdf456zxc")
print(output)