# https://www.codewars.com/kata/5ffc226ce1666a002bf023d2/train/python

# Passed

def solution(mtrx):
    result = False
    for row in mtrx:
        arrow_seen, target_seen = False, False
        for elem in row:
            if elem == ">":
                arrow_seen = True
            
            if arrow_seen and elem == "x":
                result = True
                break
        
        if result or arrow_seen:
            break
    
    return result

output = solution([
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', '>', ' ', 'x'],
  [' ', ' ', '', ' ', ' ']
])
print(output)