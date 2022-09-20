import random
import numpy as np


class Deck(object):
    def __init__(self, num_deck=1):
        # num_decks = 0 means infinite number of decks and the pick up is with replacement
        self.contents = [(2, 'Diamonds'), (2, 'Hearts'), '2 of Clubs', '2 of Spades', (3, 'Diamonds'), (3, 'Hearts'),\
                         '3 of Clubs', '3 of Spades', (4, 'Diamonds'), (4, 'Hearts'), '4 of Clubs', '4 of Spades',\
                         (5, 'Diamonds'), (5, 'Hearts'), '5 of Clubs', '5 of Spades', (6, 'Diamonds'), (6, 'Hearts'),\
                         '6 of Clubs', '6 of Spades', (7, 'Diamonds'), (7, 'Hearts'), '7 of Clubs', '7 of Spades',\
                         (8, 'Diamonds'), (8, 'Hearts'), '8 of Clubs', '8 of Spades', (9, 'Diamonds'), (9, 'Hearts'),\
                         '9 of Clubs', '9 of Spades', (10, 'Diamonds'), (10, 'Hearts'), '10 of Clubs', '10 of Spades',\
                         (11, 'Diamonds'), (11, 'Hearts'), 'Jack of Clubs', 'Jack of Spades', (12, 'Diamonds'),\
                         (12, 'Hearts'), 'Queen of Clubs', 'Queen of Spades', (13, 'Diamonds'), (13, 'Hearts'),\
                         'King of Clubs', 'King of Spades', (1, 'Diamonds'), (1, 'Hearts'), 'Ace of Clubs',\
                         'Ace of Spades']
        if num_deck is not 0:
            self.decks = [self.contents for _ in range(num_deck)]
            self.decks = list(np.concatenate(self.decks, axis=0))
        else:
            self.decks = list(self.contents)
        self.num_deck = num_deck

    def shuffle(self):
        # shuffle the cards
        random.shuffle(self.decks)

    def pop(self):
        # pop the top card out and hand it to the player
        card = self.decks.pop(0)
        # for num_deck = 0, pick up with replacement
        if self.num_deck == 0:
            self.decks = list(self.contents)
            random.shuffle(self.decks)
        return card
