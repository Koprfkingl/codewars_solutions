"""Kata - Reverse every other word in the string

completed at: 2022-12-04 21:43:23
by: Jakub Červinka

Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.

"""

from itertools import cycle 
def reverse_alternate(s):
    fn = cycle((list, reversed))
    return ' '.join(
        ''.join(next(fn)(word))
        for word in s.split()
        )
