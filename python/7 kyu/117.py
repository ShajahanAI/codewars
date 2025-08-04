# https://www.codewars.com/kata/5f55ecd770692e001484af7d/train/python

# Passed

def mirror(data: list) -> list:
    if not data:
        return data

    sorted_data = sorted(data)
    result = sorted_data[::-1]
    result = sorted_data[:-1] + result

    return result

output = mirror([-3, 15, 8, -1, 7, -1])
print(output)