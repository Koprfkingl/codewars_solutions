"""Kata - WeIrD StRiNg CaSe

completed at: 2019-03-13 12:45:36
by: Jakub Červinka

Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(`' '`). Spaces will only be present if there are multiple words. Words will be separated by a single space(`' '`).

### Examples:

```
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
```
"""

def to_weird_case(string):
    result = []
    for word in string.split(' '):    
        result.append(''.join([c.upper() if i%2 ==0 else c.lower() for i, c in enumerate(word)]))
    return ' '.join(result)
