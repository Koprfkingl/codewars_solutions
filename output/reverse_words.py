"""Kata - Reverse words

completed at: 2023-06-01 06:57:36
by: Jakub Červinka

Complete the function that accepts a string parameter, and reverses each word in the string. **All** spaces in the string should be retained.

## Examples
```
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```
"""

import re

def reverse_words(text):
    reverse = lambda m: m.group(0)[::-1]
    return re.sub(r'\S+', reverse, text)    
