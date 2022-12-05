'''
Create an initialize_deck function to initialize the deck of card tuples with 'Ace' through 'King' of each suit.
Before returning the list, use the random module’s shuffle function to randomly order the list elements. 
Output the shuffled cards in four-column format.
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
    '''Geranate the deck card tuples as "(FACE, NAIPE)"'''

    deck = list()
    for n in NAIPES:
        for f in FACES:
            deck.append((f, n))

    shuffle(deck) # Embaralha as cartas
    return deck


def pokerCardsDeal(deck):
    '''Deal a five card poker as a list of five card tuples'''

    five_cards = list()

    while len(five_cards) < 5:
        card = deck[randint(0, 51)]
        if card not in five_cards:
            five_cards.append(card)
    return five_cards

def onlyFaces(pokerHand):
    l = list()
    for item in pokerHand:
        l.append(item[0])
    return l

def onlyNaipes(pokerHand):
    l = list()
    for item in pokerHand:
        l.append(item[1])
    return l


def is_pair(pokerHand):
    '''Get five card poker hand and'''

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
    '''Get five card poker hand and'''

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
    '''Get five card poker hand and'''

    # facelist stores only faces from pokerHand tuples list
    facelist = onlyFaces(pokerHand)

    checkedFace = []
    for a in facelist:
        if (a not in checkedFace) and (facelist.count(a) == 3):
            return True
        checkedFace.append(a)
    return False


def is_straight(pokerHand):
    facelist = onlyFaces(pokerHand)

    for a in range(5):
        if FACES[a] in facelist:
            return False

    for indx in range(len(facelist)-1):
        indxInFACES = FACES.index(facelist[indx])
        if facelist[indx] != FACES[indxInFACES] or facelist[indx+1] != FACES[indxInFACES+1]:
            return False
    return True


def is_flush(pokerHand):
    naipelist = onlyNaipes(pokerHand)

    for a in range(1,5):
        if naipelist[a] != naipelist[a-1]:
            return False
    return True


def is_full_house(pokerHand):
    facelist = onlyFaces(pokerHand)
    checkedFace = list()

    for x in facelist:
        
        checkedFace.append(x)


# d = initialize_deck()
# poker = pokerCardsDeal(d)
poker = [('seis', 'Copas'), ('sete', 'Copas'), ('oito', 'Copas'), ('nove', 'Copas'), ('dez', 'Copas')]
print(poker)
print('one pair',is_pair(poker))
print('two pair', is_two_pair(poker))
print('three of kinds', is_three_of_kind(poker))
print('straight', is_straight(poker))
print('Flush', is_flush(poker))