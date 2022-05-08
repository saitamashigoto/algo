"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck

from copy import deepcopy, copy

from random import randint


class PokerHand(Hand):
    """Represents a poker hand."""

    hands_order = {'pair': 0, 'two pairs': 0, 'three of a kind': 0,
        'straight': 0, 'flush': 0, 'full house': 0, 'four of a kind': 0,
        'straight flush': 0}

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hists(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        self.rank_hists()
        for freq in self.ranks.values():
            if freq >= 2:
                return True
        return False
    
    def has_twopair(self):
        self.rank_hists()
        num_pairs = 0
        for freq in self.ranks.values():
            if freq >= 2:
                num_pairs += 1
                if num_pairs >= 2:
                    return True
        return False
    
    def has_three_of_kind(self):
        self.rank_hists()
        for freq in self.ranks.values():
            if freq >= 3:
                return True
        return False
    
    def has_four_of_kind(self):
        self.rank_hists()
        for freq in self.ranks.values():
            if freq >= 4:
                return True
        return False

    def has_straight(self):
        self.rank_hists()
        self.ranks_list = list(self.ranks.keys())
        self.ranks_list.sort()
        if 1 in self.ranks:
            return (self.detect_straight_ace_low() or self.detect_straight_ace_high())
        return self.detect_straight_ace_low() 

    def suit_ranks(self):
        self.suit_ranks = {}
        for card in self.cards:
            self.suit_ranks.setdefault(card.suit, [])
            self.suit_ranks[card.suit].append(card.rank)
        for suit in self.suit_ranks:
            self.suit_ranks[suit].sort()

    def has_straight_flush(self):
        self.suit_ranks()
        for suit in self.suit_ranks:
            self.ranks_list = self.suit_ranks[suit]
            if self.ranks_list[0] == 1:
                result = (self.detect_straight_ace_low() or self.detect_straight_ace_high())
            else:
                result = self.detect_straight_ace_low()
            if result >= 5:
                return True
        return False
        
    def detect_straight_ace_low(self):
        return self.detect_consecutive_cards()
    
    def detect_straight_ace_high(self):        
        self.ranks_list = self.ranks_list[1:]
        self.ranks_list.append(14)
        return self.detect_consecutive_cards()
    
    def detect_consecutive_cards(self):
        length = len(self.ranks_list)
        consecutive_cards = 0
        i = 0
        while (i < (length - 1)) and (consecutive_cards < 5):
            if (self.ranks_list[i+1] - self.ranks_list[i]) == 1:
                consecutive_cards += 1
            else:
                consecutive_cards = 0
            i += 1
        return consecutive_cards >= 5

    def has_full_house(self):
        self.rank_hists()
        limit = 3
        for rank, freq in self.ranks.items():
            if (limit == 3) and freq >= 3:
                limit = 2
            elif (limit == 2) and freq >= 2:
                return True
        return False

    def classify(self):
        if self.has_straight_flush():
            self.label = 'straight flush'
        elif self.has_four_of_kind():
            self.label = 'four_or_a_kind'
        elif self.has_full_house():
            self.label = 'full house'
        elif self.has_flush():
            self.label = 'flush'
        elif self.has_straight():
            self.label = 'straight'
        elif self.has_straight():
            self.label = 'straight'
        elif self.has_three_of_kind():
            self.label = 'three of a kind'
        elif self.has_twopair():
            self.label = 'two pairs'
        elif self.has_pair():
            self.label = 'pair'


def calculate_probablities():
    deck = Deck()
    deck.shuffle()
    hands_dict = {}
    hand_cards = randint(5, 52/2)
    num_hands = randint(2, 52//hand_cards) 
    print('Num Hands: %d, Hands Cards: %d' % (num_hands, hand_cards)) 
    for i in range(num_hands):
        hand = PokerHand()
        deck.move_cards(hand, hand_cards)
        hand.sort()
        hand.classify()
        hands_dict[hand.label] = hands_dict.get(hand.label, 0) + 1
    hands_probablities = {}
    print("Label           Probablity")
    for hand_label in hands_dict.keys():
        hands_probablities[hand_label] = hands_dict[hand_label] / num_hands
        hand_label_length = len(hand_label)
        print(hand_label + (' ' * (16 - hand_label_length)) + "{}".format(hands_probablities[hand_label]))

def binomial_cofficients(n, k, memo={}):
    if k == 0:
        return 1
    elif n == 0:
        return 0
    else:
        return memo.setdefault((n,k), binomial_cofficients(n-1, k) + binomial_cofficients(n-1, k-1))

if __name__ == '__main__':
   print(binomial_cofficients(randint(1, 10), randint(1, 10)))
        

