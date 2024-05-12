"""Kata - Split Strings

completed at: 2019-04-15 12:26:31
by: Jakub Červinka

Complete the solution so that it splits the string into pairs of two characters.  If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:
```
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
```

"""

def solution(s):
    from itertools import zip_longest  
    return [a + b for a, b in zip_longest(s[::2], s[1::2], fillvalue='_')]
