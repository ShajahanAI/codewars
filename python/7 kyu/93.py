# https://www.codewars.com/kata/62f96f01d67d0a0014f365cf/train/python

# Passed

def ball_test(s, r):
    while s > 0 and r:
        cracks = r[:s].count("x")
        r = r[s:]
        s -= cracks + 1

        if not r:
            # road has been completed
            return True

    return False

output = ball_test(24, 'xxxxxxxxxx_____x___xx__xx____________x__________x_')
print(output)