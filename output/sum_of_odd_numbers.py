"""Kata - Sum of odd numbers

completed at: 2023-05-30 10:33:39
by: Jakub Červinka

Given the triangle of consecutive odd numbers:

```
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
```

Calculate the sum of the numbers in the n<sup>th</sup> row of this triangle (starting at index 1) e.g.: (**Input --> Output**)

```
1 -->  1
2 --> 3 + 5 = 8
```

"""

def row_sum_odd_numbers(n):
    s = n * (n - 1) + 1
    return sum(range(s, s + 2 * n, 2))
