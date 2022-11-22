'''
Write a script that displays one of the main characters of the series and asks the user
which actor played the role.

After each question, the player is informed if their answer was correct.

At the end of the game, the number of correct guesses is displayed on the screen.
'''

import os

# Table containing Actor names and its Character
actors_char = [['Sean Bean', 'Ned Stark'], ['Mark Addy', 'Robert Baratheon'],
['Nikolaj Coster-Waldau', 'Jaime Lannister'], ['Michelle Fairley', 'Catelyn Stark'],
['Lena Headey', 'Cersei Lannister']]


correct_count = 0
for row in actors_char:
    ac, ch = row
    print(f'Which actor played the "{ch}" role?\n')

    # Actors options
    for i in actors_char:
        print(i[0])

    # User answer
    ans = str(input(': '))


    if ans == ac:
        correct_count += 1
        print('Correct!')
    else:
        print('Incorrect!')

    os.system('sleep 2')
    os.system('clear')

print(f'\n{correct_count} corret answers')