# https://www.codewars.com/kata/5672f4e3404d0609ec00000a/train/python

# Passed

def frame(text, char):
    longest_word_length = max([len(word) for word in text]) 
    longest_border = char * (longest_word_length + 4)
    
    rows = [longest_border] + [ char + " " + word + (" " * (longest_word_length - len(word))) + " " + char for word in text] + [longest_border]
    result = "\n".join(rows)
    return result

output = frame([' Create a frame!','          __     __','         /  \\~~~/  \\','   ,----(     ..    )','  /      \\__     __/',' /|         (\\  |(','^  \\  /___\\  /\\ |','   |__|   |__|-..'], '*')
print(output)