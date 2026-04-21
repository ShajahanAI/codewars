# https://www.codewars.com/kata/59ff4709ba2a14501500003a/train/python

# Passed

def arrange(arr):
    weight_str_to_kg_dict = dict()
    for weight_str in arr:
        if weight_str.endswith("KG"):
            weight = int(weight_str.replace("KG", str()))
        elif weight_str.endswith("G"):
            weight = int(weight_str.replace("G", str())) / 1000
        elif weight_str.endswith("T"):
            weight = int(weight_str.replace("T", str())) * 1000
        
        weight_str_to_kg_dict[weight_str] = weight
    
    sorted_weights = sorted(arr, key=lambda weight_str: weight_str_to_kg_dict[weight_str])
    return sorted_weights

output = arrange(["100KG","100G","150T","150KG"])
print(output)