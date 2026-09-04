# https://www.codewars.com/kata/571d2e9eeed4a150d30011e7/train/python

# Passed

class Participant:
    def __init__(self, name: str, chickenwings: int = 0, hamburgers: int = 0, hotdogs: int = 0):
        self.name = name
        self.chickenwings = chickenwings
        self.hamburgers = hamburgers
        self.hotdogs = hotdogs
        
        self.score = (self.chickenwings * 5 + 
                      self.hamburgers * 3 +
                      self.hotdogs * 2)
        
    def get_name_and_score(self) -> dict:
        return dict(name=self.name, score=self.score)
        
def scoreboard(who_ate_what):
    result = [Participant(**participant_dict).get_name_and_score() for participant_dict in who_ate_what]
    result = sorted(result, key=lambda name_and_score: (-name_and_score['score'], name_and_score['name']))
    return result

output = scoreboard([{"name": "Billy The Beast", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},
                     {"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},
                     {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
                     {"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}])
print(output)