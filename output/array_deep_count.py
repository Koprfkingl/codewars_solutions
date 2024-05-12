"""Kata - Array Deep Count

completed at: 2022-10-07 17:31:53
by: Jakub Červinka

You are given an array. Complete the function that returns the number of ALL elements within an array, including any nested arrays.


## Examples

```python
[]                   -->  0
[1, 2, 3]            -->  3
["x", "y", ["z"]]    -->  4
[1, 2, [3, 4, [5]]]  -->  7
```

The input will always be an array.

```if:php
In PHP you may *not* assume that the array passed in will be non-associative.

Please note that `count()`, `eval()` and `COUNT_RECURSIVE` are disallowed - you should be able to implement the logic for `deep_c()` yourself ;)
```

"""

def deep_count(a):
    def get_len(l):
        total = len(l)
        for e in l:
            if isinstance(e, list):
                total += get_len(e)
        return total
    return get_len(a)
    
