# https://www.codewars.com/kata/6a784d563bfd7732517d9832/train/python

# Passed

def vertical(words):
    rows = []
    if words:
        for idx in range(max(len(word) for word in words)):
            row = []
            for word in words:
                character = word[idx] if idx < len(word) else " "
                row.append(character)

            rows.append(row)
        
    result = "\n".join([" ".join(row).rstrip() for row in rows])
    return result

output = vertical(["hi", "world", "yo"])
print(output)