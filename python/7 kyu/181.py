# https://www.codewars.com/kata/5c79c07b4ba1e100097f4e1a/train/python

# Passed

def yoga(classroom, poses):
    skilled_people = 0
    for row in classroom:
        row_skill = sum(row)
        for individual_skill in row:
            total_skill = row_skill + individual_skill
            for skill_required in poses:
                if total_skill >= skill_required:
                    skilled_people += 1
    
    return skilled_people

output = yoga([
                [3,2,1,3],
                [1,3,2,1],
                [1,1,1,2],
              ],[1,7,5,9,10,21,4,3])
print(output)