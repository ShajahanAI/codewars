# https://www.codewars.com/kata/55b1fd84a24ad00b32000075/train/python

# Passed

def am_I_afraid(day,num):
    afraid_logic = {
        'Monday': lambda n: n == 12,
        'Tuesday':  lambda n: n > 95,
        'Wednesday': lambda n: n == 34,
        'Thursday': lambda n: n == 0,
        'Friday': lambda n: n % 2 == 0,
        'Saturday': lambda n: n == 56,
        'Sunday': lambda n: abs(n) == 666
    }

    return afraid_logic[day](num)

output = am_I_afraid('Monday', 12)
print(output)