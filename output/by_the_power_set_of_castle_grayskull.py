"""Kata - By the Power Set of Castle Grayskull

completed at: 2023-05-30 11:22:34
by: Jakub Červinka

Write a function that returns all of the *sublists* of a list/array.

Example:

```math
power([1,2,3]);
=> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

For more details regarding this, see the [power set][power set] entry in wikipedia.

[pure]: http://en.wikipedia.org/wiki/Pure_function
[power set]: https://en.wikipedia.org/wiki/Power_set
"""

from itertools import chain
from itertools import combinations

def power(seq):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(seq)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
