# https://www.codewars.com/kata/59f2746e50c8c2b55d000085/train/python

# Passed

def conv(num):
    digit_to_word_dict = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    num_str = str(num)
    if len(num_str) % 2 == 0:
        should_convert = lambda digit: digit % 2 == 0
        starting_lowercase = True
    else:
        should_convert = lambda digit: digit % 2 == 1
        starting_lowercase = False
    
    result = ""
    for position, digit in enumerate(map(int, num_str), start=1):
        if should_convert(digit):
            word = digit_to_word_dict[digit]
            modified_word = ""
            lowercase_word = starting_lowercase
            while position > 0:
                for idx in range(len(word)):
                    modified_word += word[idx].lower() if lowercase_word else word[idx].upper()
                    position -= 1
                    if position <= 0:
                        break
                
                lowercase_word = not lowercase_word
            
            result += modified_word
        else:
            result += str(digit)
        
    return result

output = conv(34266262106)
print(output)