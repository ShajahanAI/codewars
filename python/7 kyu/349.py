# https://www.codewars.com/kata/676474a0956b84eab4132819/train/python

# Passed

def days_of(items):
    item_counts_arr = [day_number * (len(items) - day_number + 1) for day_number in range(1, len(items) + 1)]
    result = [f"{item_count} {item}" for item_count, item in zip(item_counts_arr, items)]
    return result

output = days_of(["tree" , "bows" , "birds", "candy"])
print(output)