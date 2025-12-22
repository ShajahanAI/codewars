# https://www.codewars.com/kata/572cc218aedd20cc83000679/train/python

# Passed

def flatten(dictionary):
    flattened_dictionary = dict()
    for master_key, value in dictionary.items():
        if type(value) == dict:
            if len(value) == 0:
                flattened_dictionary[master_key] = ""
            else:
                flattened_dictionary.update({master_key + "/" + key: value for key, value in flatten(value).items()})
        else:
            flattened_dictionary[master_key] = value
            
    return flattened_dictionary
        
output = flatten({
        "additional": {
        "place": {
            "cell":"2",
            "zone":"1"
            }
        },
        "job": "scout",
        "name": {
            "last":"Drone",
            "first":"One"
            },
            "recent": {}
        })
print(output)