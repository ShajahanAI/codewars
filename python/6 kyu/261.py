# https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5/train/python

# Passed

def inside_out(strng: str) -> str:
    inside_out_word = lambda word: (word[:len(word)//2][::-1] + word[len(word)//2:][::-1]
                                    if len(word) % 2 == 0 else 
                                    word[:len(word)//2][::-1] + word[len(word)//2] + word[len(word)//2 + 1:][::-1])
    words = strng.split(' ')
    inside_out_words = [inside_out_word(word) for word in words]
    
    result = " ".join(inside_out_words)
    return result

output = inside_out('what time are we climbing up the volcano')
print(output)