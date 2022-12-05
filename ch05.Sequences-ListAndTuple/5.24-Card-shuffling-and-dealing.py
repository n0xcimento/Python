'''
Create an initialize_deck function to initialize the deck of card tuples with 'Ace' through 'King' of each suit.
Before returning the list, use the random module’s shuffle function to randomly order the list elements. 
Output the shuffled cards in four-column format.
'''

from random import shuffle

face = ['ás', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'valete', 'dama', 'rei']
naipe = ['Paus', 'Ouros', 'Copas', 'Espadas']


def display_deck(deck):
    '''Output the shuffled cards in four-column format.'''

    for indx,card in enumerate(deck):
        hold = f'{card[0]} de {card[1]}'
        print(f'{hold:20s}', end='')
        if (indx+1)%4 == 0:
            print()


def initialize_deck():
    '''Geranate the deck card as "FACE, NAIPE"'''

    deck = list()
    for n in naipe:
        for f in face:
            deck.append((f, n))

    shuffle(deck) # Embaralha as cartas
    return deck


d = initialize_deck()
# print(d)
display_deck(d)