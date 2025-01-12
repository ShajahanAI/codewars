# https://www.codewars.com/kata/5836ebe4f7e1c56e1a000033

# Passed

def combine_strings(*strings):
    if not strings:
        return str()
    
    if len (strings) == 1:
        return strings[0]

    result = ""
    lengthiest_string = max(strings, key=len) 
    max_length = len(lengthiest_string)
    for i in range(max_length):
        for string in strings:
            if len(string) > i:
                result += string[i]

    return result

interlaced_string = combine_strings("abc", "12345")
print(interlaced_string)