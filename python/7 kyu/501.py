# https://www.codewars.com/kata/6aeca9058d7577f27e2e2fbf/train/python

# Passed

from string import ascii_uppercase

def watchtower(s: str) -> str:
    indexes_to_concatenate = set()
    alphabet_to_vision_radius_dict = {
        alphabet: vision_radius for vision_radius, alphabet in enumerate(ascii_uppercase, start=1)
    }
    for idx, char in enumerate(s):
        if char.islower():
            continue
        
        vision_radius = alphabet_to_vision_radius_dict[char]
        indexes_to_concatenate.update(range(max(0, idx - vision_radius), min(idx + vision_radius + 1, len(s))))

    indexes_to_concatenate = sorted(list(indexes_to_concatenate))
    result = "".join(s[idx] for idx in indexes_to_concatenate)
    return result

output = watchtower("abAcd")
print(output)