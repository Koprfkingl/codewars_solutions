"""Kata - Exes and Ohs

completed at: 2023-05-30 13:54:56
by: Jakub Červinka

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:
```
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
```
"""

def xo(s):
    return s.lower().count('x') == s.lower().count('o')
