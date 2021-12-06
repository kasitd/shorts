from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')
Cards = 'Draw Two cards, Skip cards, Reverse cards'.split(',')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""

    u_deck_list = []

    for color in SUITS:
        u_deck_list.append(UnoCard(color, '0')) 
    
    for i in range(2): 
        for color in SUITS:    
            for i in range(13):

                if i>=1 and i <= 9 :
                    u_deck_list.append(UnoCard(color, str(i)))
                
                if i>=9 and i <=11:
                    u_deck_list.append(UnoCard(color, Cards[i-9]))
    for i in range(4):
        u_deck_list.append(UnoCard(None, name='Wild cards'))
        u_deck_list.append(UnoCard(None, name='Wild Draw Four'))              
    return u_deck_list
