# https://www.codewars.com/kata/59b06d83cf33953dbb000010/train/python

# Passed

def is_centered(xs: list[int], n: int) -> bool:
    if len(xs) % 2 == 0 and n == 0:
        return True
    
    if len(xs) % 2 == 0:
        end_idx = int(len(xs) / 2)
        start_idx = end_idx - 1
    else:
        end_idx = len(xs) // 2
        start_idx = end_idx
    
    
    for _ in range(end_idx, len(xs)):
        centered_sum = sum(xs[start_idx:end_idx+1])
        if centered_sum == n:
            return True
        
        start_idx -= 1
        end_idx += 1
    
    return False
                
output = is_centered([1,1,15,-1,-1],15)
print(output)