# https://www.codewars.com/kata/5751fef5dcc1079ac5001cff/train/python

# Passed

def err_bob(st):
    is_consonant = lambda letter: letter.lower() not in {'a', 'e', 'i', 'o', 'u'}
    words = st.split(' ')
    modified_words = []
    for word in words:
        if len(word.strip()) == 0:
            modified_words.append(word)
            continue
            
        for last_letter_idx in range(len(word) - 1, -1, -1):
            last_letter = word[last_letter_idx]
            if last_letter.isalpha():
                break
            
        if is_consonant(last_letter):
            SUFFIX = 'ERR' if last_letter.isupper() else 'err'
            word = word[:last_letter_idx + 1] + SUFFIX + word[last_letter_idx + 1:]
    
        modified_words.append(word)
        
    result = " ".join(modified_words)
    return result

output = err_bob("Punctuation? is, important!  double space also")
print(output)