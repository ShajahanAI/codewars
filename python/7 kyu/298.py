# https://www.codewars.com/kata/5669a5113c8ebf16ed00004c/train/python

# Passed

def substring_test(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if len(s1) <= 1 or len(s2) <= 1:
        return False
    
    smaller_string = s1 if len(s1) < len(s2) else s2
    larger_string = s2 if smaller_string == s1 else s1
    all_smallest_substrings = [smaller_string[idx:idx+2] for idx in range(0, len(smaller_string))]
    for substring in all_smallest_substrings:
        if len(substring) == 1:
            continue
            
        if substring in larger_string:
            return True
        
    return False

output = substring_test("Something","Home")
print(output)