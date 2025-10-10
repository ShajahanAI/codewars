# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

# Passed

def generate_hashtag(s):
    if len(s) == 0:
        return False
    
    words = s.split()
    hashtag = "#" + "".join([word.title() for word in words])
    
    if len(hashtag) > 140:
        return False
    
    return hashtag

output = generate_hashtag('Codewars Is Nice')
print(output)