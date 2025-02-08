# https://www.codewars.com/kata/5785cd91a1b8d5c06e000007/train/python

# Passed

def re_ordering(text):
    words = text.split()
    capital_word = [w for w in words if not w.islower()][0]
    capital_word_index = words.index(capital_word)

    words_reordered = [capital_word] + words[:capital_word_index] + words[capital_word_index + 1:]
    return ' '.join(words_reordered)

output = re_ordering('pl mx Lyvyclg lirofr lpzqb hmjpc')
print(output)