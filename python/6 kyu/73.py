# https://www.codewars.com/kata/52b305bec65ea40fe90007a7/train/python

# Passed

def grabscrab(said, possible_words):
    matches = []
    for word in possible_words:
        # are all letters used
        if len(said) != len(word):
            continue
        
        said_dict = dict()
        for letter in set(said):
            said_dict[letter] = said.count(letter)  

        word_dict = dict()
        for letter in set(word):
            word_dict[letter] = word.count(letter)    
        
        if said_dict == word_dict:
            matches.append(word)
            
    return matches

output = grabscrab("ortsp", ["sport", "parrot", "ports", "matey"])
print(output)