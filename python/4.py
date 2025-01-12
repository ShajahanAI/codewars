# https://www.codewars.com/kata/529b418d533b76924600085d

# Passed

def to_underscore(strng: str) -> str:
    if type(strng) != str:
        return str(strng)
    
    result = ""
    upper_indexes = []
    for idx, i in enumerate(list(strng)):
        if i.isupper():
            upper_indexes.append(idx)

    for count, index in enumerate(upper_indexes, start=1):
        if count == len(upper_indexes):
            result += strng[index:]
        else:
            result += strng[index:upper_indexes[count]] + '_'

    return result.lower()

output = to_underscore('FirstPointTheirBigTo')
print(output)
