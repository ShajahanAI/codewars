# https://www.codewars.com/kata/5c46ea433dd41b19af1ca3b3/train/python

# Passed

def hex_word_sum(s):
    words = s.split()
    hex_words = [word.upper().replace("O", "0").replace("S", "5") for word in words]
    result = 0
    for hex_word in hex_words:
        try:
            result += int(hex_word, 16)
        except ValueError as e:
            continue

    return result

output = hex_word_sum('CODE')
print(output)