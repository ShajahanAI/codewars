# https://www.codewars.com/kata/565b112d09c1adfdd500019c/train/python

# Passed

def nth_char(words):
	return ''.join([word[idx] for idx, word in  enumerate(words)])
