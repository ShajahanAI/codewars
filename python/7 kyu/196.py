# https://www.codewars.com/kata/5a3e1319b6486ac96f000049/train/python

# Passed

def pairs(arr):
    consecutive_pair_count = 0
    for idx in range(0, len(arr), 2):
        if idx + 1 == len(arr):
            break # last item
        
        if abs(arr[idx + 1] - arr[idx]) == 1:
            consecutive_pair_count += 1
            
    return consecutive_pair_count

output = pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94])
print(output)