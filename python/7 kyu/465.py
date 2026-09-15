# https://www.codewars.com/kata/5701800886306a876a001031/train/python

# Passed

def lineup_students(st):
    names = st.split(' ')
    result = sorted(names, key=lambda name: (len(name), name), reverse=True) if st else []
    return result

output = lineup_students('Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi')
print(output)