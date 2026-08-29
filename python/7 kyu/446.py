# https://www.codewars.com/kata/58cbc48930bcf09b7a000117/train/python

# Passed

def time_per_day(lst):
    total_time_in_minutes = 0
    for complexity, questions_count in lst:
        total_time_in_minutes += complexity * 0.75 * questions_count
    
    result = round(total_time_in_minutes / 300, 2)
    return result

output = time_per_day([(1, 20), (2, 10), (3, 15), (4, 10)])
print(output)