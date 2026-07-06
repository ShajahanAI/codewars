# https://www.codewars.com/kata/58844a13aa037ff143000072/train/python

# Passed

def will_you(young, beautiful, loved):
    result = False
    if young and beautiful and not loved:
        result = True
    elif loved and (not young or not beautiful):
        result = True
        
    return result

output = will_you(True, True, True)
print(output)