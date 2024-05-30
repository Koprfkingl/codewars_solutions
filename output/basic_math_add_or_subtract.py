"""Kata - Basic Math (Add or Subtract)

completed at: 2019-10-29 12:24:47
by: 

In this kata, you will do addition and subtraction on a given string. The return value must be also a string.

**Note:** the input will not be empty.

## Examples

```
"1plus2plus3plus4"  --> "10"
"1plus2plus3minus4" -->  "2"
```
"""

def calculate(s):
    # your code here
    numbers = []

    # "1plus2minus3minus4plus5minus5" -> ["1", "2minus3minus4", "5minus6"]
    for minusGroup in s.split("plus"):
        # "2minus3minus4" -> ["2", "3", "4"]
        splitMinuses = minusGroup.split("minus")

        # "2"
        plus = splitMinuses[0]
        # ["3", "4"]
        minuses = splitMinuses[1:]

        # +2
        numbers.append(int(plus))
        # -3, -4
        numbers.extend(-int(minus) for minus in minuses)




    return str(sum(numbers))
