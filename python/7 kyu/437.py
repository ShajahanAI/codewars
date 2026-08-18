# https://www.codewars.com/kata/6064c4fe71f8920036610b4b/train/python

# Passed

def post_grades(students):
    calculate_average = lambda numbers: sum(numbers) / len(numbers)
    
    result = []
    for student_data in students:
        student_id, student_name, student_marks = [datapoint.strip() for datapoint in student_data.split("-")]
        marks_average = calculate_average([float(mark) for mark in student_marks.split()])
        result.append((student_id, marks_average))
        
    result.sort(key=lambda student_id_marks_average: -student_id_marks_average[-1])
    return result

output = post_grades(['1001 - Joonghyuk Yoo - 95 98.4 92.15', '1002 - Dokja Kim - 100 96.4 90', '1003 - Boyoung Park - 84.2 90.5 92.8', '1004 - Shijin Yoo - 80 96.4 88.4'])
print(output)