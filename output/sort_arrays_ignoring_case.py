"""Kata - Sort Arrays (Ignoring Case)

completed at: 2019-11-30 20:53:06
by: Jakub Červinka

Sort the given **array of strings** in alphabetical order, case **insensitive**. For example:
```
["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]
```
"""

def sortme(words):
    return sorted(words, key=lambda x: x.lower())
