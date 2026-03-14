# https://www.codewars.com/kata/5977ef1f945d45158d00011f/train/python

# Passed

def sep_str(st): 
    words = st.split(' ')
    max_length = max([len(w) for w in words])
    result = [[] for _ in range(max_length)]
    for col_idx, word in enumerate(words):
        for row_idx in range(max_length):
            if row_idx < len(word):
                elem = word[row_idx]
            else:
                elem = str()
                
            result[row_idx].append(elem)
            
    return result

output = sep_str("The Mitochondria is the powerhouse of the cell")
print(output)