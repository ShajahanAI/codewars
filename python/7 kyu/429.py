# https://www.codewars.com/kata/57507369b0b6d1b5a60001b3/train/python

# Passed

def decompose_single_strand(single_strand):
    split_by_groups_of_three = lambda text: " ".join([text[idx:idx + 3] for idx in range(0, len(text), 3)])
    result = str()
    for frame_number in range(1, 4):
        frame = single_strand[:frame_number - 1] + " " + split_by_groups_of_three(single_strand[frame_number - 1:])
        result += f"Frame {frame_number}: {frame.strip()}\n"
    
    result = result.strip()
    return result

output = decompose_single_strand("AGGTGACACCGCAAGCCTTATATTAGC")
print(output)