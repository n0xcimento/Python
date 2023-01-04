
'''
    Script that use a dictionary to determine the numbers of votes received by candidates in an election.
'''

votes = '15,15,15,20,20,20,15,13,13,20,15,13,20'

id_qty = dict()

for vote in votes.split(','):

    if vote in id_qty:
        id_qty[vote] += 1
    else:
        id_qty[vote] = 1

for k, v in id_qty.items():
    print(f'{k:<16}{v}')