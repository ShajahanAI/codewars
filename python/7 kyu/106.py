# https://www.codewars.com/kata/58ddffda929dfc2cae0000a5/train/python

# Passed

def clonewars(kata_per_day):
    total_clones = 1
    total_kata_solved = 0
    for solutions_for_day in range(kata_per_day, 0, -1):
        total_kata_solved += total_clones * solutions_for_day
        total_clones *= 2 if solutions_for_day != 1 else 1

    result = [total_clones, total_kata_solved]
    return result

output = clonewars(5)
print(output)