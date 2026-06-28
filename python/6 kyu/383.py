# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python

# Passed

def title_case(title, minor_words=''):
    minor_words_set = set(word.lower() for word in minor_words.split(' '))
    words = title.split(' ')
    modified_words = []
    
    for idx, word in enumerate(words):
        if idx == 0:
            modified_word = word.title()
        else:
            modified_word = word.lower() if word.lower() in minor_words_set else word.title()
            
        modified_words.append(modified_word)
    
    result = " ".join(modified_words)
    return result

output = title_case('a clash of KINGS', 'a an the of')
print(output)