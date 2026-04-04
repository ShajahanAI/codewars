# https://www.codewars.com/kata/5616868c81a0f281e500005c/train/python

# Passed

from string import ascii_lowercase

def rank(st, we, n):
    participants = st.split(",")
    if len(st) == 0:
        return "No participants"
    elif n > len (participants):
        return "Not enough participants"
    
    alphabet_to_value_dict = {
        alphabet: value for value, alphabet in enumerate(ascii_lowercase, start=1)
    }
    
    winning_number_to_participants_dict = dict()
    
    for participant, weight in zip(participants, we):
        som = len(participant) + sum(alphabet_to_value_dict[char.lower()] for char in participant)
        winning_number = som * weight
        if winning_number not in winning_number_to_participants_dict:
            winning_number_to_participants_dict[winning_number] = list()
        
        winning_number_to_participants_dict[winning_number].append(participant)
        winning_number_to_participants_dict[winning_number].sort()
        
    
    ranked_participants = []
    for winning_number in sorted(winning_number_to_participants_dict.keys(), reverse=True):
        ranked_participants.extend(winning_number_to_participants_dict[winning_number])
                                     
    rank_n_participant = ranked_participants[n - 1]
    return rank_n_participant

output = rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4)
print(output)