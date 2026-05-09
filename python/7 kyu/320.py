# https://www.codewars.com/kata/57ee31c5e77282c24d000024/train/python

# Passed

def paul(x):
    label_to_score_dict = {
        'kata': 5,
        'Petes kata': 10,
        'life': 0,
        'eating': 1
    }
    
    total_score = sum([label_to_score_dict[label] for label in x])
    if total_score < 40:
        result = "Super happy!"
    elif total_score < 70:
        result = "Happy!"
    elif total_score < 100:
        result = "Sad!"
    else:
        result = "Miserable!"
        
    return result

output = paul(['life', 'Petes kata', 'Petes kata', 'Petes kata', 'eating'])
print(output)