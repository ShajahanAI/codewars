# https://www.codewars.com/kata/57f9f20004d82828c10000cd/train/python

# Passed

def from_where(you, me, question):
    if question.lower() == "where are you from?":
        for section in me:
            if me[section] != you[section]:
                answer = f"I am from {me[section]}."
                break
        else:
            answer = f"Same as you."
    elif any([question.lower() == f"what {section} are you from?".lower() for section in me.keys()]):
        # locating which section was asked
        for section in me.keys():
            if section.lower() not in question.lower():
                continue
            
            if me[section] != you[section]:
                answer = f"I am from {me[section]}."
            else:
                answer = f"Same as you."
            break
    else:
        # Invalid question
        answer = "What are you saying?"

    return answer

output = from_where({'Country': 'AA', 'Province': 'BB', 'City': 'CC', 'Town': 'DD', 'Street': 'EE'},
                    {'Country': 'AA', 'Province': 'BB', 'City': 'XX', 'Town': 'YY', 'Street': 'ZZ'}, 
                    "What country are you from?")
print(output)    