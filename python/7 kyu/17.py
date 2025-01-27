# https://www.codewars.com/kata/566efcfbf521a3cfd2000056/train/python

# Passed

def reverse_fun(n):
    # start flippin!
    for i in range(len(n)):
        n = n[:i] + ''.join(reversed(n[i:]))
    return n