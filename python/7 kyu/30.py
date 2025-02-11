# https://www.codewars.com/kata/5981a139f5471fd1b2000071/train/python

# Passed

def task(w, n, c):
    worker_map = {
        'monday': 'James',
        'tuesday': 'John',
        'wednesday': 'Robert',
        'thursday': 'Michael',
        'friday': 'William'
    }

    return f'It is {w} today, {worker_map[w.lower()]}, you have to work, you must spray {n} trees and you need {n * c} dollars to buy liquid'