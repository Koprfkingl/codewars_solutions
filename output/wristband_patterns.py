"""Kata - Wristband Patterns

completed at: 2023-06-05 19:36:35
by: Jakub Červinka

# Task
I need a wristband. Help me in identifying an actual wristband.

A wristband can have 4 patterns:

**horizontal:** each item in a row is identical.

**vertical:** each item in each column is identical.

**diagonal left:** each item is identical to the one on it's upper left or bottom right.

**diagonal right:** each item is identical to the one on it's upper right or bottom left.

Write a function that returns **True** if the section can be correctly classified into one of the 4 types, and **False** otherwise.

### Examples

####  Part of horizontal wristband
```
is_wristband([
  ["A", "A"],
  ["B", "B"],
  ["C", "C"]
]) # True 
```
#### Part of vertical wristband
```
is_wristband([
  ["A", "B"],
  ["A", "B"],
  ["A", "B"]
]) # True 
```
#### Part of diagonal left wristband
```
is_wristband([
  ["A", "B", "C"],
  ["C", "A", "B"],
  ["B", "C", "A"],
  ["A", "B", "C"]
]) # True
```
####  Part of diagonal right wristband
```
is_wristband([
  ["A", "B", "C"],
  ["B", "C", "A"],
  ["C", "A", "B"],
  ["A", "B", "A"]
]) # True
```
### Notes
- All inputs will be valid
- 1<= len(arr) <=2000

"""

from itertools import groupby
from itertools import pairwise

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def is_wristband(arr):
    is_rows = all(all_equal(row) for row in arr)
    is_cols = all(all_equal(col) for col in zip(*arr))
    is_left = all(
        a[1:] == b[:-1]
        for a, b in pairwise(arr)
    )
    is_right = all(
        a[:-1] == b[1:]
        for a, b in pairwise(arr)
    )
    return any((
        is_rows,
        is_cols,
        is_left,
        is_right,
    ))
