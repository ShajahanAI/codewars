# https://www.codewars.com/kata/6885f0a045008e707baa714b/train/python

# Passed

def read(tape, head, moves):
    indexes_to_read = []
    for move in moves:
        indexes_to_read.append(head)

        if move == ">":
            head += 1
        elif move == "<":
            head -= 1
        
    result = "".join([tape[idx] for idx in indexes_to_read])
    return result
        
output = read('011010', 3, '>><<')
print(output)