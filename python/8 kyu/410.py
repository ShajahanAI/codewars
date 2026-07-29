# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

# Passed

def lovefunc(flower1, flower2):
    result = (flower1 + flower2) % 2 != 0
    return result

output = lovefunc(1,4)
print(output)