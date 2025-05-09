# https://www.codewars.com/kata/590f5b4a7bbb3e246000007d/train/python

# Passed

def comes_after(st, l):
    result = str()
    while st:
        if l.lower() not in st.lower():
            break # no more occurences of l
        
        after_idx = st.lower().find(l.lower()) + 1
        if after_idx == len(st):
            # no characters after letter
            break

        result += st[after_idx] if st[after_idx].isalpha() else str()
        st = st[after_idx:]        

    return result

output = comes_after("Free coffee for all office workers!", 'F')
print(output)