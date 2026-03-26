# https://www.codewars.com/kata/597a660f59873cc353000061/train/python

# Passed

def get_colors(col_arr):
    get_max_colour_channel_idx = lambda colour_code: max(enumerate([int(colour_code[idx:idx+2], 16) for idx in range(0, len(colour_code), 2)]),
                                                     key=lambda idx_colour_channel_val: idx_colour_channel_val[1])[0]
    idx_to_colour_channel_dict = {
        0: 'Red',
        1: 'Green',
        2: 'Blue'
    }
    
    major_minor_channel_combos = []
    for colour_code_sub_arr in col_arr:
        max_rgb_count_arr = [0, 0, 0]
        for colour_code in colour_code_sub_arr:
            max_colour_channel_idx = get_max_colour_channel_idx(colour_code)
            max_rgb_count_arr[max_colour_channel_idx] += 1
        
        maj_idx_maj_val = max(enumerate(max_rgb_count_arr), key=lambda idx_rgb_count: idx_rgb_count[1])
        maj_idx, maj_val = maj_idx_maj_val
        major_channel = idx_to_colour_channel_dict[maj_idx]
        
        min_idx_min_val = min(enumerate(max_rgb_count_arr), key=lambda idx_rgb_count: idx_rgb_count[1])
        min_idx, min_val = min_idx_min_val
        if min_val == 0:
            # that means not present at all, looking for next largest
            min_idx = list({0, 1, 2} - {min_idx, maj_idx})[0]
            min_val = max_rgb_count_arr[min_idx]

        minor_channel = idx_to_colour_channel_dict[min_idx]
        major_minor_channel_combos.append(major_channel + "+" + minor_channel)
        
    result = ",".join(major_minor_channel_combos)
    return result

output = get_colors([
    ["6B8E23", "9ACD32","2E8B57","00008B", "00FF00","6B8E23","00FA9A"],
    [ "CD5C5C", "8B0000", "FF0000", "F08080", "98FB98", "DC143C"],
    [ "00BFFF", "00008B", "B22222", "000080", "87CEEB", "4169E1"]
    ])
print(output)