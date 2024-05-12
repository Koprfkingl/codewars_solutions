"""Kata - Exclamation marks series #7: Remove words from  the sentence if it contains one exclamation mark 

completed at: 2022-05-31 11:07:08
by: Jakub Červinka

# Description:

Remove words from the sentence if they contain exactly one exclamation mark. Words are separated by a single space, without leading/trailing spaces.

# Examples

```
remove("Hi!") === ""
remove("Hi! Hi!") === ""
remove("Hi! Hi! Hi!") === ""
remove("Hi Hi! Hi!") === "Hi"
remove("Hi! !Hi Hi!") === ""
remove("Hi! Hi!! Hi!") === "Hi!!"
remove("Hi! !Hi! Hi!") === "!Hi!"
```

"""

def remove(s):
    correct = []
    for word in s.split():
        if word.count('!') != 1:
            correct.append(word)
    return ' '.join(correct)
