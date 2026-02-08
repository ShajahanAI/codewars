# https://www.codewars.com/kata/5b047875de4c7f9af800011b/train/python

# Passed

def sentence(lst):
    combined_dict = {}
    for word_dict in lst:
        combined_dict.update(word_dict)
        
    keys = [int(key) for key in list(combined_dict.keys())]
    keys.sort()
    
    words = []
    for key in keys:
        word = combined_dict[str(key)]
        words.append(word)
        
    sentence = " ".join(words)
    return sentence

output = sentence([{'3': 'Jake.'}, {'5': 'Chinatown'}, {'1': 'Forget'}, {'4': 'It is'}, {'2': 'it'}])
print(output)