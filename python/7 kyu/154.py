# https://www.codewars.com/kata/57d532d2164a67cded0001c7/train/python

# Passed

def histogram(results):
    dice_to_frequency_dict = {
        dice_num: frequency for dice_num, frequency in enumerate(results, start=1) 
    }
    
    histogram_string = ""
    for dice_num in range(6, 0, -1):
        frequency = dice_to_frequency_dict[dice_num]
        if frequency > 0:
            histogram_string += f"{dice_num}|{'#' * frequency} {frequency}".strip() + "\n"
        else:
            histogram_string += f"{dice_num}|{'#' * frequency}".strip() + "\n"
            
    return histogram_string

output = histogram([7,3,10,1,0,5])
print(output)