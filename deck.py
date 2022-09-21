import random
import numpy as np


class Deck(object):
    def __init__(self, num_deck=1, is_black_jack = True):
        # num_decks = 0 means infinite number of decks and the pick up is with replacement
        self.contents = [(2, 'Diamonds'), (2, 'Hearts'), (2, 'Clubs'), (2, 'Spades'), (3, 'Diamonds'), (3, 'Hearts'),\
                         (3, 'Clubs'), (3, 'Spades'), (4, 'Diamonds'), (4, 'Hearts'), (4, 'Clubs'), (4, 'Spades'),\
                         (5, 'Diamonds'), (5, 'Hearts'), (5, 'Clubs'), (5, 'Spades'), (6, 'Diamonds'), (6, 'Hearts'),\
                         (6, 'Clubs'), (6, 'Spades'), (7, 'Diamonds'), (7, 'Hearts'), (2, 'Clubs'), '7 of Spades',\
                         (8, 'Diamonds'), (8, 'Hearts'), (8, 'Clubs'), (8, 'Spades'), (9, 'Diamonds'), (9, 'Hearts'),\
                         (9, 'Clubs'), (9, 'Spades'), (10, 'Diamonds'), (10, 'Hearts'), (10, 'Clubs'), (10, 'Spades'),\
                         (11, 'Diamonds'), (11, 'Hearts'), (11, 'Clubs'), (11, 'Spades'), (12, 'Diamonds'),\
                         (12, 'Hearts'), (12, 'Clubs'), (12, 'Spades'), (13, 'Diamonds'), (13, 'Hearts'),\
                         (13, 'Clubs'), (13, 'Spades'), (1, 'Diamonds'), (1, 'Hearts'), (1, 'Clubs'),\
                         (1, 'Spades')]
        if num_deck is not 0:
            self.decks = [self.contents for _ in range(num_deck)]
            self.decks = list(np.concatenate(self.decks, axis=0))
        else:
            self.decks = list(self.contents)
        self.num_deck = num_deck
        self.is_black_jack = is_black_jack

    def shuffle(self):
        # shuffle the cards
        random.shuffle(self.decks)
    
    def reset(self):
        self.decks = list(self.contents)
        random.shuffle(self.decks)

    def pop(self):
        # pop the top card out and hand it to the player
        card = self.decks.pop(0)
        if self.is_black_jack and card[0]>10:
            card = (10, card[1])
        # for num_deck = 0, pick up with replacement
        if self.num_deck == 0:
            self.reset()
        return card
