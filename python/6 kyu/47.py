# https://www.codewars.com/kata/58de77a2c19f096a5a00013f/train/python

# Passed

def find_added(st1, st2):
    st1_dict = {char: st1.count(char) for char in set(st1)}
    st2_dict = {char: st2.count(char) for char in set(st2)}
    
    st2_numbers = [int(num) for num in set(st2)]
    st2_numbers.sort()
    result = str()
    for number in st2_numbers:
        number = str(number)
        result += number * (st2_dict[number] - st1_dict.get(number, 0))
        
    return result

output = find_added('9876521', '9876543211')
print(output)