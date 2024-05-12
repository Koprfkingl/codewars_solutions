"""Kata - Break camelCase

completed at: 2020-04-05 18:16:15
by: Jakub Červinka

Complete the solution so that the function will break up camel casing, using a space between words.

### Example 

```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```
"""

def solution(st):
    import re
    to_join = [s for s in re.split("([A-Z][^A-Z]*)", st) if s]
    return ' '.join(to_join)
