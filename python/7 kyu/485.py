# https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/python

# Passed

class Dictionary():
    def __init__(self):
        self.dictionary = dict()
        
    def newentry(self, word, definition):
        self.dictionary[word] = definition
        
    def look(self, key):
        return self.dictionary.get(key, f"Can't find entry for {key}")

output = Dictionary()
output.newentry("Apple", "A fruit")
print(output.look("Apple"))