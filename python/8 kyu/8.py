# https://www.codewars.com/kata/596fba44963025c878000039

# Passed

def contamination(text, char):
    if not text or not char:
        return str()
    
    return char * len(text)

output = contamination('abc', 'z')
print(output)