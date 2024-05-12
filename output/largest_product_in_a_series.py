"""Kata - Largest product in a series

completed at: 2023-05-30 11:27:57
by: Jakub Červinka

Complete the `greatestProduct` method so that it'll find the greatest product of five consecutive digits in the given string of digits.

For example: the greatest product of five consecutive digits in the string `"123834539327238239583"` is 3240.

The input string always has more than five digits.

Adapted from Project Euler.
"""

import collections
from itertools import islice
import functools
import operator

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

def greatest_product(n):
    return max(
        functools.reduce(operator.mul, map(int, window))
        for window in sliding_window(n, 5)
    )
