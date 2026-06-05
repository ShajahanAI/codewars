# https://www.codewars.com/kata/5751aa92f2dac7695d000fb0/train/python

# Passed

def beasts(heads, tails):    
    hydra = (heads - 2 * tails) / 3
    orthus = tails - hydra
    
    result = [int(orthus), int(hydra)] if hydra >= 0 and orthus >= 0 and\
                                int(hydra) == hydra and int(orthus) == orthus else 'No solutions'
    
    return result

output = beasts(123, 39)
print(output)