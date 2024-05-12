"""Kata - Consecutive strings

completed at: 2022-09-10 19:43:54
by: Jakub Červinka

You are given an array(list) `strarr` of strings and an integer `k`. Your task is to return the **first** longest string
consisting of k **consecutive** strings taken in the array.

#### Examples:
```
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
```
n being the length of the string array, if `n = 0` or `k > n` or `k <= 0` return "" (return `Nothing` in Elm, "nothing" in Erlang).

#### Note
consecutive strings : follow one after another without an interruption
"""

import collections
from itertools import islice

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

def longest_consec(strarr, k):
    
    if not strarr or not (0 < k < len(strarr)):
        return ''
    
    strings = [''.join(tup) for tup in sliding_window(strarr, k)]

    return sorted(strings, key=len, reverse=True)[0]
    
    
