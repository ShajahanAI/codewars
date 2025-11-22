# https://www.codewars.com/kata/557592fcdfc2220bed000042/train/python

# Passed

def pattern(n: int) -> str:
    cycles = []
    numbers = [str(n) for n in range(1, n + 1)]
    for idx in range(n):
        idx %= len(numbers)
        cycle_pattern = "".join(numbers[idx:]) + "".join(numbers[:idx])
        cycles.append(cycle_pattern)
        
    result = "\n".join(cycles)
    return result

output = pattern(11)
print(output)