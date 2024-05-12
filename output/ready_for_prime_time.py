"""Kata - (Ready for) Prime Time

completed at: 2022-10-08 20:37:19
by: Jakub Červinka

We need prime numbers and we need them now!

Write a method that takes a maximum bound and returns all primes up to and including the maximum bound.

For example,

```
11 => [2, 3, 5, 7, 11]
```
"""

def prime(n):
    if n in (0, 1): return []
    n += 1
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i]=[False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]
