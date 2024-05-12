"""Kata - Numericals of a String

completed at: 2023-06-22 12:30:11
by: Jakub Červinka

You are given an input string.

For each symbol in the string if it's the first character occurrence, replace it with a '1', else replace it with the amount of times you've already seen it.

___

## Examples:

```
input   =  "Hello, World!"
result  =  "1112111121311"

input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"
```

There might be some non-ascii characters in the string.

<hr>

~~~if:java
Note: there will be no int domain overflow (character occurrences will be less than 2 billion).
~~~
~~~if:c
(this does not apply to the C language translation)
~~~


Take note of **performance**

"""

from collections import defaultdict

def numericals(s):
    memory = defaultdict(lambda: 1)
    
    def get_count(char):
        count = memory[char]
        memory[char] += 1
        return count
    
    return ''.join(str(get_count(c)) for c in s)
