'''
Write a script that randomly generates a list containing 8000 user IDs using random letters from the range "a" through "f" and
numbers from the range 1 to 4.
'''

import random


def remove_duplicate(arg):
    new_list = []

    for a in arg:
        if a not in new_list:
            new_list.append(a)

    return new_list


# usersId is the list that will contain all userId generated
usersId = []
for a in range(800):
    userId = random.choice('abcdef') + ''.join(random.choices('1234', k=2))
    usersId.append(userId)


usersId = remove_duplicate(remove_duplicate(usersId))
usersId.sort()
for i, a in enumerate(usersId):
    print(f'{a}\t', end='')

    if (i+1)%10 == 0: print()

print()