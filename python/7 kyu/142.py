# https://www.codewars.com/kata/55c353487fe3cc80660001d4/train/python

# Passed

def capitals_first(text):
    words = text.split()
    uppercase_words = [word for word in words if word[0].isupper()]
    lowercase_words = [word for word in words if word[0].islower()]
    sorted_str = " ".join(uppercase_words + lowercase_words)
    return sorted_str

output = capitals_first("hey You, Sort me Already")
print(output)