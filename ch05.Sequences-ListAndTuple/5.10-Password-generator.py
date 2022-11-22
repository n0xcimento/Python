'''
Write a script that generates all possible passwords based on a given string consisting of two
letters and one digit.
'''

import itertools

user_in = str(input('two letters ; one digit: '))

print('possible passwords: ')
for a in itertools.permutations(user_in, 3):
    print(''.join(a), end=' ') # Convert tuple to string

print()