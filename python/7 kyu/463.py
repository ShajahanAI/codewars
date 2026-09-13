# https://www.codewars.com/kata/582c297e56373f0426000098/train/python

# Passed

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: Node):
    numbers = []
    while node and node.next:
        numbers.append(node.data)
        node = node.next
    
    if node:
        numbers.append(node.data)

    numbers.append(None)
    result = " -> ".join(map(str, numbers))
    return result

output = stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))
print(output)