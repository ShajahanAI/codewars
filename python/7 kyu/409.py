# https://www.codewars.com/kata/576bb3c4b1abc497ec000065/train/python

# Passed

def compare(s1, s2):
    def calculate_score(text):
        score = 0
        if not text:
            return score

        for char in text:
            if not char.isalpha():
                return 0
            
            score += ord(char.upper())
            
        return score

    result = calculate_score(s1) == calculate_score(s2)
    return result

output = compare("AD", "BC")
print(output)