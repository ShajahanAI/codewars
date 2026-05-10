# https://www.codewars.com/kata/609eee71109f860006c377d1/train/python

# Passed

def last_survivor(letters, coords):
    arr = list(letters)
    for idx in coords:
        del arr[idx]
        
    result = "".join(arr)
    return result

output = last_survivor('zbk', [2, 1])
print(output)