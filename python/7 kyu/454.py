# https://www.codewars.com/kata/54d22119beeaaaf663000024/train/python 

# Passed

def shades_of_grey(n):
    result = []
    for num in range(1, min(n, 254) + 1):
        hexadecimal_component = hex(num)
        result.append(f"#{hexadecimal_component.split('x')[-1].zfill(2) * 3}")
        
    return result

output = shades_of_grey(10)
print(output)