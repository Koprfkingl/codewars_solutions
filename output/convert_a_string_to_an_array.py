"""Kata - Convert a string to an array

completed at: 2019-10-30 15:36:42
by: 

Write a function to split a string and convert it into an array of words.

### Examples (Input ==> Output):

```
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
```

```if:c
Words will be separated by exactly one space, without leading or trailing spaces.

There will only be letters and spaces in the input string.
```

"""

def string_to_array(s):
    # your code here
    a = s.split(' ')
    return a
