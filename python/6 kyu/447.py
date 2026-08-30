# https://www.codewars.com/kata/5aa69e68ba1bb5ecdf000557/train/python

# Passed

def longest_sequence(n: int) -> list[int]:
    square_root = n ** 0.5
    sequences = []
    num_to_square_dict = dict()
    for start_num in range(1, int(square_root) + 1):
        current_sum = 0
        for num in range(start_num, int(square_root) + 1):
            if num in num_to_square_dict:
                num_squared = num_to_square_dict[num]
            else:
                num_squared = num ** 2
                num_to_square_dict[num] = num_squared
                
            current_sum += num_squared
            if current_sum == n:
                sequences.append(list(range(start_num, num + 1)))
                break
            elif current_sum > n:
                break
    
    result = max(sequences, default=[], key=lambda sequence: len(sequence))
    return result

output = longest_sequence(595)
print(output)