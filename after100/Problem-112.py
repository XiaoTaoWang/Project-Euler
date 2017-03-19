# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 12:04:38 2017

@author: XiaoTao Wang
"""

"""
Problem 112: Bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half
of the numbers below one-thousand (525) are bouncy. In fact, the least number
for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

"""
# The concept of "bouncy number" seems quite straightforward, so it's easy to
# write a function to check if an positive integer is a bouncy number
def isBouncy(n):
    
    inc = False
    dec = False
    
    main, last = divmod(n, 10)
    while main > 0:
        main, mod = divmod(main, 10)
        if mod < last:
            inc = True
        elif mod > last:
            dec = True
        if inc and dec:
            return True
        
        last = mod
    
    return (inc and dec)

def work():
    
    total = 99
    bouncy = 0
    while 100*bouncy < 99*total:
        total += 1
        if isBouncy(total):
            bouncy += 1
    
    return total

if __name__ == '__main__':
    total = work() # ~1.91s
    