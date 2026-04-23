# https://www.codewars.com/kata/69e8cd7f48dd4ffb1d25ef2f/train/python

# Passed

def rumor_starter(record):
    all_people_who_were_told_the_rumor_set = set()
    for people_who_were_told_the_rumor_arr in record.values():
        all_people_who_were_told_the_rumor_set.update(people_who_were_told_the_rumor_arr)
    
    people_who_started_the_rumor = list()
    for person in record:
        if person not in all_people_who_were_told_the_rumor_set:
            people_who_started_the_rumor.append(person)
            
    people_who_started_the_rumor.sort()
    return people_who_started_the_rumor

output = rumor_starter({"Haley":["Steph"], "Josh":["Ava"], "Kate":["Ava","Josh","Mia"], "Kim":["Ava","Josh","Mia"], "Ava":[], "Elly":["Kim"], "Mia":[]})
print(output)