# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:24:43 2016

@author: Xiaotao Wang
"""

"""
Problem 84:

In the game, Monopoly, the standard board is set up in the following way:

...Omitted figure...

A player starts on the GO square and adds the scores on two 6-sided dice to
determine the number of squares they advance in a clockwise direction. Without
any further rules we would expect to visit each square with equal probability:
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance)
changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player
to go directly to jail, if a player rolls three consecutive doubles, they do not
advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player
lands on CC or CH they take a card from the top of the respective pile and,
after following the instructions, it is returned to the bottom of the pile.
There are sixteen cards in each pile, but for the purpose of this problem we
are only concerned with cards that order a movement; any instruction not concerned
with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
1.Advance to GO
2.Go to JAIL
Chance (10/16 cards):
1.Advance to GO
2.Go to JAIL
3.Go to C1
4.Go to E3
5.Go to H2
6.Go to R1
7.Go to next R (railway company)
8.Go to next R
9.Go to next U (utility company)
10.Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll. For
this reason it should be clear that, with the exception of G2J for which the
probability of finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square, and it is the final
square that the player finishes at on each roll that we are interested in. We
shall make no distinction between "Just Visiting" and being sent to JAIL, and
we shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with sets
of squares.

Statistically it can be shown that the three most popular squares, in order,
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00.
So these three most popular squares can be listed with the six-digit modal string:
102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the
six-digit modal string.

"""
# The most appropriate approach I can come up with is Simulation.
# Implement all the rules given above, perform the game several times(100),
# one time for 1000 rolls, and we can approximate the probability of each
# square easily.
import random, collections, time

# Game settings ...
dice = range(1, 5)
squares = [('GO',0), ('A',1), ('CC',1), ('A',2), ('T',1), ('R',1), ('B',1),
           ('CH',1), ('B',2), ('B',3), ('JAIL',0), ('C',1), ('U',1), ('C',2),
           ('C',3), ('R',2), ('D',1), ('CC',2), ('D',2), ('D',3), ('FP',0),
           ('E',1), ('CH',2), ('E',2), ('E',3), ('R',3), ('F',1), ('F',2),
           ('U',2), ('F',3), ('G2J',0), ('G',1), ('G',2), ('CC',3), ('G',3),
           ('R',4), ('CH',3), ('H',1), ('T',2), ('H',2)]
stoidx = dict(zip(squares, range(len(squares))))
idxtos = {v:k for k,v in stoidx.items()}

def ccpile():
    cards = [None] * 16 + [('GO',0), ('JAIL',0)]
    random.shuffle(cards)
    while True:
        for card in cards:
            yield card

def chpile():
    cards = [None] * 6 + [('GO',0), ('JAIL',0), ('C',1), ('E',3), ('H',2),
                          ('R',1), ('next R',), ('next R',), ('next U',),
                          ('back 3',)]
    random.shuffle(cards)
    while True:
        for card in cards:
            yield card

def makerolls(dice, num):
    res = []
    for i in range(num):
        res.append(random.choice(dice))
    return res

# Start game ...
def singleroll(oridx, cc, ch):
    tmpidx = oridx % 40
    s = idxtos[tmpidx]
    if s == ('G2J',0):
        return stoidx[('JAIL',0)]
    elif s[0] in ['CC','CH']:
        if s[0] == 'CC':
            card = cc.next()
        else:
            card = ch.next()
        tmp = stoidx.get(card)
        if not tmp is None:
            return tmp
        else:
            if card == None:
                return tmpidx
            if card == ('back 3',):
                # Although unnecessary to this special problem, recursion
                # exists generally
                return singleroll(oridx-3, cc, ch)
            if card in [('next R',), ('next U',)]:
                check = card[0].split()[1]
                while s[0] != check:
                    oridx += 1
                    s = idxtos[oridx%40]
                return stoidx[s]
    else:
        return tmpidx
        
def simulation(times, rolls):
    statistic = collections.defaultdict(float)
    for t in xrange(times):
        # Shuffle the CC and CH cards
        cc = ccpile()
        ch = chpile()
        idx = 0 # We start at GO
        three = [] # Three consecutive doubles?
        for i in xrange(rolls):
            roll = makerolls(dice, 2)
            double_check = (roll[0]==roll[1])
            if len(three) < 2:
                three.append(double_check)
            else:
                if all(three) and double_check:
                    idx = stoidx[('JAIL',0)]
                    statistic[idx] += 1
                    three = []
                    continue
                else:
                    three[0] = three[1]
                    three[1] = double_check
            tmpidx = idx+sum(roll) # May exceed 39
            idx = singleroll(tmpidx, cc, ch)
            statistic[idx] += 1
    
    for idx in statistic:
        statistic[idx] = statistic[idx] / (times*rolls)
    
    return statistic

if __name__ == '__main__':
    start = time.time()
    stats = simulation(100, 1000)
    reverse_view = {v:k for k,v in stats.items()}
    elapse = time.time() - start
    print('Time elapse: %.4gs' % elapse)
    