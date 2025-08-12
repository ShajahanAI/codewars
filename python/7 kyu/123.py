# https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/python

# Passed

def consecutive(arr, a, b):
    for idx, elem in enumerate(arr):
        if elem == a or elem == b:
            adjacent_elem_to_check = a if elem == b else b
            indexes_to_check = []
            if idx == 0:
                indexes_to_check.append(idx + 1)
            elif idx == len(arr) - 1:
                indexes_to_check.append(idx - 1)
            else:
                indexes_to_check.extend([idx - 1, idx + 1])

            for idx in indexes_to_check:
                if arr[idx] == adjacent_elem_to_check:
                    return True

    return False

output = consecutive([1, 3, 5, 7], 3, 1)
print(output)