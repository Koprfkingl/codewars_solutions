"""Kata - Find the unique string

completed at: 2022-10-09 20:30:14
by: Jakub Červinka

There is an array of strings. All strings contains similar _letters_ except one. Try to find it!

```javascript
findUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) === 'BbBb'
findUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) === 'foo'
```

```php
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]); // => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]); // => 'foo'
```

```python
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
```

```cobol
      FindUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])
      * => result = 'BbBb'
      FindUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])
      * => result = 'foo'
```

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.

This is the second kata in series:

1. [Find the unique number](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)
2. Find the unique string (this kata)
3. [Find The Unique](https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)
"""

from collections import Counter
def find_uniq(arr):
    c = Counter((frozenset(a.strip().lower()) for a in arr))
    lowest = next(k for k, v in c.items() if v == 1)
    for a in arr:
        if set(a.strip().lower()) == lowest:
            return a

