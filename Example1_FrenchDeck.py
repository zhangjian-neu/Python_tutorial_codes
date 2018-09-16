# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:41:07 2018

@author: zhj
"""

import collections
Card = collections.namedtuple('Card',['rank', 'suit'])
from random import choice

class FrenchDeck(): 
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()  
    
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
# sort according to some rules
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

    
if __name__ == "__main__":
    deck = FrenchDeck()
    print(deck[0])
    print(len(deck))
    print(choice(deck))
    print(deck[0:3])
    
    for card in sorted(deck, key=spades_high):
        print(card)