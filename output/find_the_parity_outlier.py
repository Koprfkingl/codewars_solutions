"""Kata - Find The Parity Outlier

completed at: 2019-03-05 11:45:46
by: Jakub Červinka

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.

## Examples

```
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
```

"""

def find_outlier(lst):
    lst.sort(key = lambda x: x % 2)
    return lst[-1] if lst[0]%2 == lst[1]%2 else lst[0]
    
