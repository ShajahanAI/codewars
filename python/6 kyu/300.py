# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python

# Passed

def rev_rot(strng, sz):
    if sz <= 0 or sz > len(strng) or strng == "":
        result = str()
        return result
    
    chunks = [strng[idx:idx+sz] for idx in range(0, len(strng), sz)]
    modified_chunks = []
    for chunk in chunks:
        if len(chunk) < sz:
            continue
        
        chunk_sum = sum([int(digit) for digit in chunk])
        if chunk_sum % 2 == 0:
            modified_chunk = chunk[::-1]
        else:
            modified_chunk = chunk[1:] + chunk[0]

        modified_chunks.append(modified_chunk)

    result = "".join(modified_chunks)
    return result

output = rev_rot("733049910872815764", 5)
print(output)