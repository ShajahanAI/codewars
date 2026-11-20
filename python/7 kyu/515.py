# https://www.codewars.com/kata/54582f970a80d2ca46000f25/train/python

# Passed

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = " ".join([self.first_name, self.last_name])
    
    def greet(self):
        return f"Hello, {self.full_name}!"

output = Person('Bob', 'Smith').greet()
print(output)