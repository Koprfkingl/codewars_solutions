"""Kata - Find the stray number

completed at: 2023-06-17 13:31:47
by: Jakub Červinka

You are given an *odd-length* array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

**The input array will always be valid!** (odd-length >= 3)

## Examples

```
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
```
"""

from collections import Counter

def stray(arr):
    c = Counter(arr)
    return next(k for k, v in c.items() if v == 1)
