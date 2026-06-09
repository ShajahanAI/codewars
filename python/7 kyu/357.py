# https://www.codewars.com/kata/5a4d303f880385399b000001/train/python

# Passed

def strong_num(number):
    def calculate_factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        
        return result

    total_sum = sum(calculate_factorial(int(digit)) for digit in str(number))
    is_strong_num = total_sum == number
    
    result = "STRONG!!!!" if is_strong_num else "Not Strong !!"
    return result

output = strong_num(145)
print(output)