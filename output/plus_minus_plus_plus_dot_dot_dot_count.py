"""Kata - Plus - minus - plus - plus - ... - Count

completed at: 2019-02-24 17:52:44
by: Jakub Červinka

Count how often sign changes in array.

### result

number from `0` to ... . Empty array returns `0`

### example

```javascript
const arr = [1, -3, -4, 0, 5];

/*
| elem | count |
|------|-------|
|  1   |  0    |
| -3   |  1    |
| -4   |  1    |
|  0   |  2    |
|  5   |  2    |
*/

catchSignChange(arr) == 2;
```

~~~if:lambdacalc
### encodings

purity: `LetRec`  
numEncoding: <span style="color: aqua">extended</span> `binaryScott`  
export constructors `nil, cons` for your `List` encoding

* <span style="color: aqua">negative numbers</span> are allowed, encoded as the bit-complement of the encoding of their absolute value
* e.g. `6 -> 011$ ; -6 -> 100$`
* non-negative number encoding is unchanged
* the normal invariant "MSB, if any, must be `1`" becomes "MSB must be `0`" for negative numbers
* you can use positive, zero and negative number literals in your code
* return value is a non-negative `Number`, in basic Binary Scott encoding
~~~
"""

def catch_sign_change(lst):
    from itertools import groupby
    return 0 if len(lst) == 0 else len([sum(g) for _, g in groupby(lst, key=lambda x: x < 0)])-1
