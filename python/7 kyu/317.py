# https://www.codewars.com/kata/5a5bef7a5c770d08cd0032fa/train/python

# Passed

def agents(list_found, list_records):
    result = "No matches"
    if list_found:
        for rec in list_records:
            if rec == list_found:
                result = "Match found"
                break
    else:
        result = None
            
    return result

output = agents(["Sally", "David", "Jack", "Rebeccah"], [["Sally", "David", "Jack", "Rebeccah"], ["Jennie", "Jill", "Frank"]])
print(output)