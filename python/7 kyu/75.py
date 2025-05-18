# https://www.codewars.com/kata/56ce2f90aa4ac7a4770019fa/train/python

# Passed

def evenator(s):
    characters_to_remove = ".,?!_"
    for char in characters_to_remove:
        s = s.replace(char, str())
    
    cleansed_words = list()
    for word in s.split():
        if len(word) % 2 != 0:
            # it's a odd length word
            word += word[-1]
        cleansed_words.append(word)

    result = " ".join(cleansed_words)
    return result

output = evenator('I got a hole in 1!')
print(output)