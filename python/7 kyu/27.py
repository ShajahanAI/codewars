# https://www.codewars.com/kata/679e0a54f8d448b508865c3b/train/python

# Passed

def estimator(obstacles, stamina):
    consecutive_ones_count = 0
    stamina_tracker = []
    obstacles += [0] # so that the loop doesn't end abruptly
    for obstacle in obstacles:
        if obstacle == 1:
            consecutive_ones_count += 1 
        elif consecutive_ones_count:
            stamina_tracker.append(2 if consecutive_ones_count == 1 else (consecutive_ones_count - 1) * 5)
            consecutive_ones_count = 0
        
    return sum(stamina_tracker) <= stamina
           
output = estimator([0, 1, 0, 0, 0, 0, 1], 3)
print(output)