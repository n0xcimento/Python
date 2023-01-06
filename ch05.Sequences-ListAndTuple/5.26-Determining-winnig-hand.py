'''
[CHALLENGE]
Create an initialize_deck function to initialize the deck of card tuples with 'ás' through 'rei' of each suit.
Before returning the list, use the random module’s shuffle function to randomly order the list elements. 
Output the shuffled cards in four-column format.

Create a function that deal a five-card poker hand as a list of five card tuples. Then create functions
that determine whether the hand they receive as an argument contains patterns to win.

Write a script that deals two five-card poker hands, evaluates each hand and determines which wins.
As each card is dealt, it should be removed from the deck.
'''

from random import shuffle, randint
from operator import itemgetter

FACES = ['ás', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'valete', 'dama', 'rei']
NAIPES = ['Paus', 'Ouros', 'Copas', 'Espadas']
HAND_RANK = ['One Pair', 'Two Pair', 'Three of Kind', 'Straight', 'Flush', 'Full House',\
             'Four of a Kind', 'Straight Flush']


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


def display_deck(deck):
    '''Output the shuffled cards in four-column format.'''

    for indx,card in enumerate(deck):
        hold = f'{card[0]} de {card[1]}'
        print(f'{hold:20s}', end='')
        if (indx+1)%4 == 0:
            print()

def display_pokerHand(pokerHand):
    '''Display the card as "FACE de SUITE"'''

    for card in pokerHand:
        faceSuite = ''.join([card[0], ' de ', card[1]])
        print(f'|{faceSuite:^17}|')


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
    '''Deal a Poker hand of five cards as a list of tuples from the deck.'''

    five_cards = list()

    while len(five_cards) < 5:
        card = flushed_deck[randint(0, len(flushed_deck)-1)]
        flushed_deck.remove(card)
        five_cards.append(card)

    five_cards.sort(key=itemgetter(1))
    return five_cards


def is_one_pair(pokerHand):
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
    if (not is_flush(pokerHand)) or (not is_straight(pokerHand)):
        return False
    return True


def evaluationHand(pokerHand):
    '''Evaluate the rank of the gived poker hand.'''

    if is_straight_flush(pokerHand):
        return 7
    elif is_four_of_kind(pokerHand):
        return 6
    elif is_full_house(pokerHand):
        return 5
    elif is_flush(pokerHand):
        return 4
    elif is_straight(pokerHand):
        return 3
    elif is_three_of_kind(pokerHand):
        return 2
    elif is_two_pair(pokerHand):
        return 1
    elif is_one_pair(pokerHand):
        return 0
    else:
        return -1


def display_player(player_id, pokerHand):
    player = ''.join(['Player ', player_id])
    print(f'+{"-"*17}+')
    print(f'|{player:^17}|')
    print(f'+{"-"*17}+')
    display_pokerHand(pokerHand)


def main():

    flushed_deck = initialize_deck()
    hand1 = pokerCardDeal(flushed_deck)
    hand2 = pokerCardDeal(flushed_deck)
    a = evaluationHand(hand1)
    b = evaluationHand(hand2)

    display_player('0x1', hand1)
    display_player('0x2', hand2)

    if a > b:
        print(f'\nPlayer 0x1 won with [{HAND_RANK[a]}]')
    elif a < b:
        print(f'\nPlayer 0x2 won with [{HAND_RANK[b]}]')
    else:
        print(f'\nNo winner')


if __name__ == '__main__':
    main()