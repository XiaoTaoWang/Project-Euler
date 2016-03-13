# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 18:09:33 2016

@author: wxt
"""

"""
Problem 19:

You are given the following information, but you may prefer to do some research
for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

"""
# Since there's no more interesting tricks except brute forcing to solve this
# problem, I'll use Python's calendar package for convenience.
import calendar

count = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        monthdays = calendar.monthcalendar(year, month)
        if monthdays[0][-1] == 1:
            count += 1

print count