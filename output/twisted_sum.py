"""Kata - Twisted Sum

completed at: 2023-05-24 17:50:23
by: Jakub Červinka

Find the sum of the digits of all the numbers from `1` to `N` (both ends included).

## Examples

```
# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
```

"""

def compute_sum(n):
    sum_num = lambda n: sum(map(int, str(n)))
    return sum(map(sum_num, range(n + 1)))
