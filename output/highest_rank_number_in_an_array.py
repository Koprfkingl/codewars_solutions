"""Kata - Highest Rank Number in an Array

completed at: 2022-09-06 17:53:42
by: Jakub Červinka

Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.


## Examples

```
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
```

"""

def highest_rank(arr):
    from collections import Counter
    c = Counter(arr)
    vals = sorted(c.items(), key=lambda kv: (-kv[1], -kv[0]))
    return vals[0][0]
