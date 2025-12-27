# https://www.codewars.com/kata/56684677dc75e3de2500002b/train/python

# Passed

def comfortable_word(word):
    left = set("q, w, e, r, t, a, s, d, f, g, z, x, c, v, b".split(", "))
    right = set("y, u, i, o, p, h, j, k, l, n, m".split(", "))
    
    current_set = left if word[0] in left else right
    for letter in word:
        if letter not in current_set:
            return False
        
        current_set = right if current_set == left else left
        
    return True

output = comfortable_word('yams')
print(output)