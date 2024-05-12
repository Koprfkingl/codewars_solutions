"""Kata - Decipher this! 

completed at: 2023-05-04 07:07:16
by: Jakub Červinka

You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:
- the second and the last letter is switched (e.g. `Hello` becomes `Holle`)
- the first letter is replaced by its character code (e.g. `H` becomes `72`)

* there are no special characters used, only letters and spaces
* words are separated by a single space
* there are no leading or trailing spaces

Examples
```
'72olle 103doo 100ya' --> 'Hello good day'
'82yade 115te 103o'   --> 'Ready set go'
```

"""

import re

def unscramble(word):
    
    _, num_str, rest = re.split(r'(\d+)', word)
    first_char = chr(int(num_str))
    
    lr = len(rest)
    
    if lr == 0:
        return first_char
    if lr == 1:
        return first_char + rest
    if lr == 2:
        return first_char + rest[-1] + rest[0]
    return first_char + rest[-1] + rest[1:-1] + rest[0]


def decipher_this(s):
    return ' '.join(unscramble(word) for word in s.split())
    
