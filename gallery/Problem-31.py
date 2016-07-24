# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 19:15:45 2016

@author: wxt
"""

"""
Problem 31:

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

"""
currency = {u'£2': 200, u'£1': 100, '50p': 50, '20p': 20,
             '10p': 10, '5p': 5, '2p': 2, '1p': 1}
reverse = {currency[k]:k for k in currency}

# There're two schemes
# The first one is straightforward but looks ugly and hard to be extended
def bruteforce(coin):
    
    total = currency[coin]
    a = total
    count = 0
    
    while a >= 0:
        b = a
        while b >= 0:
            c = b
            while c >= 0:
                d = c
                while d >= 0:
                    e = d
                    while e >= 0:
                        f = e
                        while f >= 0:
                            g = f
                            while g >= 0:
                                count += 1
                                g -= 2
                            f -= 5
                        e -= 10
                    d -= 20
                c -= 50
            b -= 100
        a -= 200
    
    return count

# The second one uses dynamic programming. It's much more elegant
def dynamic(coin):
    
    total = currency[coin]
    
    pieces = sorted(reverse)
    counts = [0 for i in range(total+1)]
    counts[0] = 1
    for p in pieces:
        for med in range(p, total+1):
            counts[med] += counts[med-p]
    
    return counts[-1]


if __name__ == '__main__':
    print bruteforce(u'£2')
    print dynamic(u'£2')
            