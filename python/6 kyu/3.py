# https://www.codewars.com/kata/578597a122542a7d24000018/train/python

# Failed (by timeout)

def is_happy(n, pow):
    result = [n]
    powers = dict() # to store the powers in memory
    starting_number = n
    while len(result) == 1 or starting_number != n:    
        digit_powers = []
        for digit in str(n):
            if powers.get(digit):
                digit_powers.append(powers[digit])
                continue
            
            raised_value = int(digit) ** pow
            digit_powers.append(raised_value)
            powers[digit] = raised_value

        n = sum(digit_powers)
        result.append(n)

        if n == 1:
            return [1]
    
    return result

output = is_happy(42, 2)
print(output)
    
