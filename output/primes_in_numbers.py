"""Kata - Primes in numbers

completed at: 2020-11-14 19:11:46
by: Jakub Červinka

Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :
```
 "(p1**n1)(p2**n2)...(pk**nk)"
```
with the p(i) in increasing order and n(i) empty if
n(i) is 1.
```
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
```


"""

def prime_factors(num):
    from collections import Counter
    
    def primefac(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    
    factors = Counter(primefac(num))
    result = ''.join(
        f'({num}**{power})' if power > 1 else f'({num})'
        for num, power in sorted(factors.items(), key=lambda x: x[0])
        )
    return result
