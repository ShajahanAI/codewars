# https://www.codewars.com/kata/57fe7ea808d102a2ba000edd/train/python

# Passed

def pluralize(word):
    es_plurals = ["s", "x", "z", "ch", "sh"]
    vowels = "aeiou"
    if any([word.endswith(i) for i in es_plurals]):
        word = word + "es"
    elif word[-2] not in vowels and word[-1] == "y":
        word = word[:-1] + "ies"
    else:
        word += "s"

    return word

output = pluralize('buzz')
print(output)