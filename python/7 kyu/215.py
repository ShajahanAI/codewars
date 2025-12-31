# https://www.codewars.com/kata/56a628758f8d06b59800000f/train/python

# Passed

def self_descriptive(num):
    counter_dict = dict()
    for digit in str(num):
        if digit not in counter_dict:
            counter_dict[digit] = 0
            
        counter_dict[digit] = str(int(counter_dict[digit]) + 1)

    for n in range(len(str(num))):
        if counter_dict.get(str(n), "0") != str(num)[n]:
            return False
    return True

output = self_descriptive(21200)
print(output)