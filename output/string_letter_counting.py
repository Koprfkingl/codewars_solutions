"""Kata - String Letter Counting

completed at: 2020-05-08 19:13:33
by: Jakub Červinka

Take an input string and return a string that is made up of the number of occurences of each english letter in the input followed by that letter, sorted alphabetically. The output string shouldn't contain chars missing from input (chars with 0 occurence); leave them out.

An empty string, or one with no letters, should return an empty string.

Notes:

* the input will always be valid;
* treat letters as **case-insensitive**


## Examples

```
"This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
""                          ==>  ""
"555"                       ==>  ""
```
"""

def string_letter_count(s):
    from collections import Counter, OrderedDict
    from string import ascii_letters
    c = OrderedDict(sorted(Counter(s.lower()).items()))
    return ''.join(f'{v}{k}' for k, v in c.items() if k in ascii_letters)
    
