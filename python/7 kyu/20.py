# https://www.codewars.com/kata/5390bac347d09b7da40006f6/solutions/python

# Passed

def to_jaden_case(string):
    return ' '.join([word[0].upper() + word[1:] for word in string.lower().split(' ')])

output = to_jaden_case("How can mirrors be real if our eyes aren't real")
print(output)