"""Kata - Sequences and Series

completed at: 2023-05-30 10:42:07
by: Jakub Červinka

Have a look at the following numbers.

```
 n | score
---+-------
 1 |  50
 2 |  150
 3 |  300
 4 |  500
 5 |  750
```

Can you find a pattern in it? If so, then write a function `getScore(n)`/`get_score(n)`/`GetScore(n)` which returns the score for any positive number `n`.


___Note___
Real test cases consists of 100 random cases where `1 <= n <= 10000`


"""

def get_score(n):
    return n * (n + 1) * 25
