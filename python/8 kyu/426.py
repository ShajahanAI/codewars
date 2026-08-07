# https://www.codewars.com/kata/56530b444e831334c0000020/train/python

# Passed

def chromosome_check(chromosome):
    offspring_sex = "son" if chromosome == "XY" else "daughter"
    result = f'Congratulations! You\'re going to have a {offspring_sex}.'
    return result

output = chromosome_check('XY')
print(output)