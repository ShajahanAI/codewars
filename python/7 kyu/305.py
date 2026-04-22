# https://www.codewars.com/kata/5b6375f707a2664ada00002a/train/python

# Passed

def who_is_online(friends):
    activity_dict = dict()
    for friend in friends:
        friend_status = friend['status']
        friend_name = friend['username']
        if friend_status == 'online':
            last_activity = friend['last_activity']
            if last_activity > 10:
                friend_status = 'away'
                
        if friend_status not in activity_dict:
            activity_dict[friend_status] = list()
            
        activity_dict[friend_status].append(friend_name)
        
    return activity_dict

output = who_is_online([
    {"username": "David","status": "online","last_activity": 10},
    {"username": "Lucy","status": "online","last_activity": 0},
    {"username": "Bob","status": "online","last_activity": 3},
    {"username": "Julie","status": "offline","last_activity": 104},
    {"username": "Lenny","status": "online","last_activity": 38}]
)
print(output)