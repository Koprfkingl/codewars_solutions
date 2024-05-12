"""Kata - Number of trailing zeros of N!

completed at: 2019-04-15 13:18:57
by: Jakub Červinka

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

`N! = 1 * 2 * 3 *  ... * N`

Be careful `1000!` has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html 

## Examples

```python
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
```

*Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.*
"""

def zeros(n):
    from itertools import takewhile, count
    return sum(takewhile(lambda x: x >= 1, (n//(5**i) for i in count(1))))
    
