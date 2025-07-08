# https://www.codewars.com/kata/57f7796697d62fc93d0001b8/train/python

# Passed

def trouble(x, t):
    while True:
        indexes_to_delete = set()
        contain_pairs = False
        for idx, num in enumerate(x):
            if idx >= len(x) - 1:
                break

            if x[idx] + x[idx + 1] == t and idx not in indexes_to_delete:
                indexes_to_delete.add(idx + 1)
                contain_pairs = True
        
        if not contain_pairs:
            result = x
            break

        result = [num for idx, num in enumerate(x) if idx not in indexes_to_delete]
        x = result

    return result

output = trouble([4, 1, 1, 1, 4], 2)
print(output)