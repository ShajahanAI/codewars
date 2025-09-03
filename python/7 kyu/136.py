# https://www.codewars.com/kata/599db0a227ca9f294b0000c8/train/python

# Passed

def test(r):
    results_dict = dict(h=0, a=0, l=0)
    marks_sum = 0
    for mark in r:
        if mark <= 6:
            results_dict['l'] += 1
        elif mark <= 8:
            results_dict['a'] += 1
        else:
            results_dict['h'] += 1
            
        marks_sum += mark
        
    class_average = round(marks_sum/len(r), 3)
    report = [class_average, results_dict]
    if results_dict['h'] == len(r):
        report.append('They did well')
        
    return report

output = test([10,9,9,10,9,10,9])
print(output)