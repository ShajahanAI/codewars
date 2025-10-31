# https://www.codewars.com/kata/595d4823c31ba629d90000d2/train/python

# Passed

def find_rarest_pepe(pepes):
    pepes_counter = dict()
    for pepe in pepes:
        if pepe not in pepes_counter:
            pepes_counter[pepe] = 0
            
        pepes_counter[pepe] += 1
    
    rarest_pepe_count = float("inf")
    for pepe in pepes_counter:
        if pepes_counter[pepe] < rarest_pepe_count:
            rarest_pepe_count = pepes_counter[pepe]
            
    if rarest_pepe_count >= 5:
        return "No rare pepes!"
    
    rarest_pepes = [pepe for pepe in pepes_counter if pepes_counter[pepe] == rarest_pepe_count]
    if len(rarest_pepes) == 1:
        return rarest_pepes[0]
    
    rarest_pepes.sort()
    return rarest_pepes

output = find_rarest_pepe(
    [
    'Deep Learning Pepe',
    'Go Pepe',
    'Machine Learning Pepe',
    'Machine Learning Pepe',
    'Machine Learning Pepe'
    ]
)
print(output)