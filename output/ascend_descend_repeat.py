"""Kata - Ascend,  Descend,  Repeat?

completed at: 2023-11-26 13:59:29
by: Jakub Červinka

You are given three integer inputs: length, minimum, and maximum.

Return a string that:
1. Starts at minimum
2. Ascends one at a time until reaching the maximum, then
3. Descends one at a time until reaching the minimum
4. repeat until the string is the appropriate length

Examples:

```
 length: 5, minimum: 1, maximum: 3   ==>  "12321"
 length: 14, minimum: 0, maximum: 2  ==>  "01210121012101"
 length: 11, minimum: 5, maximum: 9  ==>  "56789876567"
```
Notes:
- length will always be non-negative
- negative numbers can appear for minimum and maximum values
- hyphens/dashes ("-") for negative numbers do count towards the length
- the resulting string must be truncated to the exact length provided
- return an empty string if maximum < minimum or length == 0
- minimum and maximum can equal one another and result in a single number repeated for the length of the string

"""

from itertools import islice
from itertools import chain
from itertools import cycle

def ascend_descend(length, minimum, maximum):
    if minimum == maximum:
        return str(minimum) * length
    up = range(minimum, maximum)
    down = range(maximum, minimum, -1)
    it = cycle(chain(up, down))
    res_it = islice(it, 0, length)
    s = ''.join(map(str, res_it))
    return s[:length]
                   

