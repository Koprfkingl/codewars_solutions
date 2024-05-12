"""Kata - Are we alternate?

completed at: 2023-09-04 19:43:04
by: Jakub Červinka

Create a function `isAlt()` that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.

```javascript
isAlt("amazon")
// true
isAlt("apple")
// false
isAlt("banana")
// true
```
```haskell
isAlt "amazon" -> True
isAlt "apple"  -> False
isAlt "banana" -> True
```
```python
is_alt("amazon")  # True
is_alt("apple")   # False
is_alt("banana")  # True
```
```csharp
Kata.IsAlt("amazon")
// true
Kata.IsAlt("apple")
// false
Kata.IsAlt("banana")
// true
```
```coffeescript
isAlt 'amazon'
# true
isAlt 'apple'
# false
isAlt 'banana'
# true
```

Arguments consist of only lowercase letters.
"""

from itertools import pairwise

def is_alt(s):
    bools = (c in 'aeiou' for c in s)
    return not any(a == b for a, b in pairwise(bools))
