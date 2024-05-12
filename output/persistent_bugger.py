"""Kata - Persistent Bugger.

completed at: 2019-03-06 11:42:14
by: Jakub Červinka

Write a function, `persistence`, that takes in a positive parameter `num` and returns its multiplicative persistence, which is the number of times you must multiply the digits in `num` until you reach a single digit.

For example **(Input --> Output)**:

```
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
```

"""

def persistence(n):
    from itertools import count
    from functools import reduce
    c = count(0)
    while len(str(n)) > 1:
        n = str(reduce(lambda x, y: int(x)*int(y), str(n)))        
        next(c)
    return next(c)
