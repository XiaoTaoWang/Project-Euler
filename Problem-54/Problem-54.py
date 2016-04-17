# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:03:10 2016

@author: Xiaotao Wang
"""

"""
Problem 54:

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players have
a pair of queens, then highest cards in each hand are compared (see example
4 below); if the highest cards tie then the next highest cards are compared,
and so on.

Consider the following five hands dealt to two players:
Hand	 	Player 1	 	     Player 2	 	     Winner
1	 	5H 5C 6S 7S KD     2C 3S 8S 8D TD    Player 2
       Pair of Fives      Pair of Eights
	 	 	
2	 	5D 8C 9S JS AC     2C 5C 7D 8S QH    Player 1
      Highest card Ace  Highest card Queen
	 	 	
3	 	2D 9C AS AH AC     3D 6D 7D TD QD    Player 2
         Three Aces     Flush with Diamonds
	 	 	
4	 	4D 6S 9H QH QC     3D 6D 7H QD QS    Player 1
       Pair of Queens     Pair of Queens
     Highest card Nine  Highest card Seven
	 	 	
5	 	2H 2D 4C 4D 4S     3C 3D 3S 9S 9D    Player 1
         Full House         Full House
      With Three Fours   with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?

"""
# Poker suit:
# Spade -- S, Heart -- H, Diamond -- D, Club -- C

from operator import itemgetter

def genGames(filename):
    
    value_mapping = {'A':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
                     '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13}
    
    with open('p054_poker.txt', 'r') as F:
        for line in F:
            parse = line.rstrip().split()
            part1 = [(value_mapping[i[0]], i[1]) for i in parse[:5]]
            part2 = [(value_mapping[i[0]], i[1]) for i in parse[5:]]
            yield part1, part2

class Cards(object):
    
    def __init__(self, cards):
        
        f = itemgetter(0)
    
        cards.sort(key=f)
        self.cards = cards
    
        Table = {}
    
        sorted_values = tuple(map(f, cards))
        suits = tuple(map(itemgetter(1), cards))
        set_size = {s:sorted_values.count(s) for s in set(sorted_values)}
    
        if (sorted_values==(10,11,12,13,14)) and (len(set(suits))==1):
            Table[9] = 1 # Royal Flush
        else:
            Table[9] = 0
    
        diff = [(sorted_values[i]-sorted_values[i-1])==1 for i in range(1, 5)]
        if all(diff) and (len(set(suits))==1):
            Table[8] = 1 # Straight Flush
        else:
            Table[8] = 0
            
        if sorted(set_size.values()) == [1, 4]:
            Table[7] = 1 # Four of a Kind
        else:
            Table[7] = 0
    
        if sorted(set_size.values()) == [2, 3]:
            Table[6] = 1 # Full House
            
        else:
            Table[6] = 0
    
        if len(set(suits))==1:
            Table[5] = 1 # Flush
        else:
            Table[5] = 0
    
        if all(diff):
            Table[4] = 1 # Straight
        else:
            Table[4] = 0
    
        if max(set_size.values()) == 3:
            Table[3] = 1 # Three of a Kind
        else:
            Table[3] = 0
    
        if list(set_size.values()).count(2) == 2:
            Table[2] = 1 # Two Pairs
        else:
            Table[2] = 0
    
        if max(set_size.values()) == 2:
            Table[1] = 1 # One Pair
        else:
            Table[1] = 0
    
        value_class = [(i,(set_size[i], i)) for i in sorted_values]
        value_class.sort(key = itemgetter(1), reverse = True)
        Table[0] = tuple(map(f, value_class))
        
        self.Table = Table
    
    def _compari(self, other):
        label = 0
        for k in sorted(self.Table, reverse=True):
            if self.Table[k] > other.Table[k]:
                label = 1
                break
            elif self.Table[k] < other.Table[k]:
                label = -1
                break
        return label
    
    def __eq__(self, other):
        return self._compari(other) == 0
    def __ne__(self, other):
        return self._compari(other) != 0
    
    def __gt__(self, other):
        return self._compari(other) == 1
    
    def __lt__(self, other):
        self._compari(other) == -1
    
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    
def workcore(filename):
    
    games = genGames(filename)
    count = 0
    win = 0
    for g in games:
        count += 1
        player_1 = Cards(g[0])
        player_2 = Cards(g[1])
        if player_1 > player_2:
            win += 1
    
    return count, win

if __name__ == '__main__':
    res = workcore('p054_poker.txt')