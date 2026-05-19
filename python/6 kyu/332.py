# https://www.codewars.com/kata/55031bba8cba40ada90011c4/train/python

# Passed

def is_sum_of_cubes(s):
    is_cubic = lambda num_group: sum(int(digit) ** 3 for digit in num_group) == int(num_group)
    current_group = str()
    number_groups = []
    for char in s:
        if char.isdigit() and len(current_group) < 3:
            current_group += char
        elif current_group:
            number_groups.append(current_group)
            current_group = char if char.isdigit() else str()
    
    if current_group:
        number_groups.append(current_group)
    
    cubic_groups = [number_group for number_group in number_groups if is_cubic(number_group)]
    result = "Unlucky"
    if len(cubic_groups) > 0:
        cubic_groups_sum = sum(int(cubic_group) for cubic_group in cubic_groups)
        result = f"{' '.join(cubic_groups)} {cubic_groups_sum} Lucky"
        
    return result

output = is_sum_of_cubes("&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()")
print(output)