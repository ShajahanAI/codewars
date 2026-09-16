# https://www.codewars.com/kata/58305403aeb69a460b00019a/train/python

# Passed

def reverse_and_mirror(s1, s2):
    def invert_case(string):
        inverted_case_string = str()
        for char in string[::-1]:
            if char.isupper():
                char = char.lower()
            else:
                char = char.upper()
            
            inverted_case_string += char
        return inverted_case_string
    
    separator = "@@@"
    s1_inverted = invert_case(s1[::-1])
    s2_inverted = invert_case(s2)
    result = s2_inverted + separator + s1_inverted[::-1] + s1_inverted
    return result

output = reverse_and_mirror('String Reversing', 'Changing Case')
print(output)