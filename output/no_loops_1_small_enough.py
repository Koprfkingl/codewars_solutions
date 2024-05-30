"""Kata - No Loops 1 - Small enough?

completed at: 2019-08-29 09:30:24
by: 

*** No Loops Allowed ***

You will be given an array (a) and a limit value (limit). You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.

Do not use loops. Do not modify input array.

Looking for more, loop-restrained fun? Check out the other kata in the series:

<a> https://www.codewars.com/kata/no-loops-2-you-only-need-one</a>

<a> https://www.codewars.com/kata/no-loops-3-copy-within</a>
"""

def small_enough(a, limit):
    # your code here
    if max(a) <= limit:
        return True
    else:
        return False
