#!/usr/bin/python3

"""A simple pythonic deck that implements the __getitem__ and __len__ special
methods, making it a sequence. Put another way, the basic sequence protocol
implements __getitem__ and __len__.

Page 4.

Using FrenchDeck
=================

>>> deck = FrenchDeck()
>>> len(deck)
52

>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1] 
Card(rank='A', suit='hearts')

Slicing also works
>>> deck[:2]
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades')]
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]
