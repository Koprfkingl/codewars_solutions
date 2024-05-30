"""Kata - No Loops 2 - You only need one

completed at: 2020-07-13 06:58:53
by: 

*** No Loops Allowed ***

You will be given an array `a` and a value `x`. All you need to do is check whether the provided array contains the value, without using a loop.

Array can contain numbers or strings. `x` can be either. Return `true` if the array contains the value, `false` if not. With strings you will need to account for case.

Looking for more, loop-restrained fun? Check out the other kata in the series:

[No Loops 1 - Small enough?](https://www.codewars.com/kata/no-loops-1-small-enough)
"""

def check(a, x): 
    # your code here
    if x in a:
        return True
    else:
        return False
