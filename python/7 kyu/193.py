# https://www.codewars.com/kata/57fcaed83206fb15fd00027a/train/python

# Passed

def replace_nth(text, n, old_value, new_value):
    if n <= 0:
        return text
    
    altered_text = str()
    old_value_count = 0
    for char in text:
        if char == old_value:
            old_value_count += 1
            if old_value_count % n == 0:
                char = new_value
        
        altered_text += char
        
    return altered_text

output = replace_nth("Vader said: No, I am your father!", 2, 'a', 'o')
print(output)