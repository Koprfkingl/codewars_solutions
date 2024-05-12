"""Kata - Count characters in your string

completed at: 2019-04-02 12:41:59
by: Jakub Červinka

The main idea is to count all the occurring characters in a string. If you have a string like `aba`, then the result should be `{'a': 2, 'b': 1}`.

What if the string is empty? Then the result should be empty object literal, `{}`.
"""

def count(string):
    from collections import Counter
    return Counter(string)
