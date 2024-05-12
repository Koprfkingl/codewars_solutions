"""Kata - Vowel Count

completed at: 2019-03-01 08:57:28
by: Jakub Červinka

Return the number (count) of vowels in the given string. 

We will consider `a`, `e`, `i`, `o`, `u` as vowels for this Kata (but not `y`).

The input string will only consist of lower case letters and/or spaces.

"""

def getCount(inStr):
    return sum([1 for c in inStr if c in 'aeiou'])
