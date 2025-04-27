# https://www.codewars.com/kata/572b82bf4903c13b1b001079/train/python

# Passed

def deaf_grandma(you):
    grandmas_replies = []
    for sentence in you:
        if sentence.isupper():
            if sentence == "BYE":
                # end the conversation
                grandmas_replies.append("OK, BYE!")
                break
                
            # you're shouting
            grandmas_replies.append("NO, NOT SINCE 1938!")
        else:
            grandmas_replies.append("HUH?! SPEAK UP, SONNY!")
            
    return grandmas_replies

output = deaf_grandma(["hi grandma", "WHAT", "bye", "BYE"])
print(output)