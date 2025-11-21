# https://www.codewars.com/kata/587a75dbcaf9670c32000292/train/python

# Passed

def filter_words(st):
    words = st.split()
    words_to_join = [words[0].title()] + [word.lower() for word in words[1:]]
    cleansed_sentence = " ".join(words_to_join)
    return cleansed_sentence

output = filter_words('NOW THIS is a VERY EXCITING test!')
print(output)