'''
[CHALLENGE]
Create an initialize_deck function to initialize the deck of card tuples with 'ás' through 'rei' of each suit.
Before returning the list, use the random module’s shuffle function to randomly order the list elements. 
Output the shuffled cards in four-column format.

Create a function that deal a five-card poker hand as a list of five card tuples. Then create functions
that determine whether the hand they receive as an argument contains patterns to win.
'''

from random import shuffle, randint

FACES = ['ás', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'valete', 'dama', 'rei']
NAIPES = ['Paus', 'Ouros', 'Copas', 'Espadas']


def display_deck(deck):
    '''Output the shuffled cards in four-column format.'''

    for indx,card in enumerate(deck):
        hold = f'{card[0]} de {card[1]}'
        print(f'{hold:20s}', end='')
        if (indx+1)%4 == 0:
            print()


def initialize_deck():
    '''Initialie the deck of card tuple with 'ás' through 'rei' of each suit. So, geranate the
    deck card as a list of tuples as "(FACE, NAIPE)" and flush the deck.'''

    deck = list()
    for n in NAIPES:
        for f in FACES:
            deck.append((f, n))

    shuffle(deck) # Embaralha as cartas
    return deck


def pokerCardDeal(flushed_deck):
    '''Deal a Poker hand of five cardas as a list of tuples.'''

    five_cards = list()

    while len(five_cards) < 5:
        card = flushed_deck[randint(0, 51)]
        if card not in five_cards:
            five_cards.append(card)
    return five_cards


def onlyFaces(pokerHand):
    l = list()
    for item in pokerHand:
        # face from tuple (FACE, NAIPE)
        l.append(item[0])
    return l


def onlyNaipes(pokerHand):
    l = list()
    for item in pokerHand:
        # naipe from tuple (FACE, NAIPE)
        l.append(item[1])
    return l


def is_pair(pokerHand):
    '''A hand that contains two cards of one rank and three cards of three other ranks.'''

    # facelist stores only faces from pokerHand tuples list
    facelist = onlyFaces(pokerHand)

    pair_count = 0
    checkedFace = []
    for a in facelist:
        if (a not in checkedFace) and (facelist.count(a) == 2):
            pair_count += 1
        checkedFace.append(a)
    return pair_count == 1


def is_two_pair(pokerHand):
    '''A hand that contains two cards of one rank, two cards of another rank and one card of a third rank.'''

    # facelist stores only faces from pokerHand tuples list
    facelist = onlyFaces(pokerHand)

    pair_count = 0
    checkedFace = []
    for a in facelist:
        if (a not in checkedFace) and (facelist.count(a) == 2):
            pair_count += 1
        checkedFace.append(a)
    return pair_count == 2


def is_three_of_kind(pokerHand):
    '''A hand that contains three cards of one rank and two cards of two other ranks.'''

    # facelist stores only faces from pokerHand tuples list
    facelist = onlyFaces(pokerHand)

    checkedFace = []
    for a in facelist:
        if (a not in checkedFace) and (facelist.count(a) == 3):
            return True
        checkedFace.append(a)
    return False


def is_straight(pokerHand):
    '''A hand that contains five cards of sequential rank, not all of the same suit.'''

    facelist = onlyFaces(pokerHand)
    facelist_index = []

    # Cria uma lista de indices das faces da mão de poker
    facelist_index = [FACES.index(a) for a in facelist]
    facelist_index.sort()

    # Para validar o caso de ás-alto
    if (12 in facelist_index) and (0 in facelist_index):
        facelist_index.remove(0)
        facelist_index.append(13)

    # Com a lista de indexes ordenada, verifica se está em ordem e com difernça de 1 entre os indexes.
    for a in range(1, 5):
        if facelist_index[a-1] != facelist_index[a] - 1:
            return False
    return True


def is_flush(pokerHand):
    '''A hand that contains five cards all of the same suit, not all of sequential rank.'''

    naipelist = onlyNaipes(pokerHand)

    if naipelist.count(naipelist[0]) != 5:
        return False
    return True


def is_full_house(pokerHand):
    '''A hand that contains three cards of one rank and two cards of another rank.'''

    facelist = onlyFaces(pokerHand)
    facelist.sort()
    checkedFace = []
    faceQty = []

    for a in facelist:
        if a not in checkedFace:
            faceQty.append((a, facelist.count(a)))
            checkedFace.append(a)
    return (faceQty[0][1] == 3 and faceQty[1][1] == 2) or (faceQty[0][1] == 2 and faceQty[1][1] == 3)


def is_four_of_kind(pokerHand):
    '''A hand that contains four cards of one rank and one card of another rank.'''

    facelist = onlyFaces(pokerHand)

    for a in facelist:
        if facelist.count(a) == 4:
            return True
        return False


def is_straight_flush(pokerHand):
    '''A straight flush is a hand that contains five cards of sequential rank, all of the same suit.'''
    
    # if the poker hand is a flush and is a straight, then the poker hand is a straight-flush
    if (not is_flush(poker)) or (not is_straight(pokerHand)):
        return False
    return True


# d = initialize_deck()
# poker = pokerCardDeal(d)
poker = [('rei', 'Paus'), ('dez', 'Paus'), ('ás', 'Paus'), ('dama', 'Paus'), ('valete', 'Paus')]
print(poker)
print('one pair',is_pair(poker))
print('two pair', is_two_pair(poker))
print('three of kinds', is_three_of_kind(poker))
print('straight', is_straight(poker))
print('Flush', is_flush(poker))
print('Full House', is_full_house(poker))
print('Four of a kind', is_four_of_kind(poker))
print('Straight Flush', is_straight_flush(poker))