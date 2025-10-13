# https://www.codewars.com/kata/570fd7ad34e6130455001835/train/python

# Passed

def zebulans_nightmare(function):
    header_words = function.split("_")
    camel_case_header_words = header_words[:1] + [header_word.title() for header_word in header_words[1:]]
    camel_case_header = "".join(camel_case_header_words)
    return camel_case_header

output = zebulans_nightmare('convert_to_uppercase')
print(output)