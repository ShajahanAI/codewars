# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

# Passed

def longest(a1, a2):
    all_unique_letters = set(a1).union(set(a2))
    sorted_letters = sorted(list(all_unique_letters))
    result = "".join(sorted_letters)
    
    return result

output = longest("loopingisfunbutdangerous", "lessdangerousthancoding")
print(output)