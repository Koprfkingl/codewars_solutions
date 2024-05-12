"""Kata - Seven Segment Display

completed at: 2024-01-07 20:38:28
by: Jakub Červinka

A **Seven Segment Display** is an electronic display device, used to display decimal or hexadecimal numerals. It involves seven led segments that are lit in specific combinations to represent a specific numeral. An example of each combination is shown below:

![seven segment display](https://upload.wikimedia.org/wikipedia/commons/9/97/7-segments_Indicator.gif)

For this Kata, you must accept an integer in the range `0 - 999999` and print it as a string (in decimal format), with each digit being represented as its own seven segment display (6x seven segment displays in total). Each of the individual led segments per display should be represented by three hashes `###`. Vertical bars `|` (ASCII 124) represent the edges of each display, with a single whitespace on either side between the edge and the area of the led segments. An example of the expected output is shown below:
```
segment_display(123456) = 
|       |  ###  |  ###  |       |  ###  |  ###  | 
|     # |     # |     # | #   # | #     | #     |
|     # |     # |     # | #   # | #     | #     |
|     # |     # |     # | #   # | #     | #     |
|       |  ###  |  ###  |  ###  |  ###  |  ###  |
|     # | #     |     # |     # |     # | #   # |
|     # | #     |     # |     # |     # | #   # |
|     # | #     |     # |     # |     # | #   # |
|       |  ###  |  ###  |       |  ###  |  ###  |
```
For clarity, the entire set of required combinations is provided below:

```
|  ###  |       |  ###  |  ###  |       |  ###  |  ###  |  ###  |  ###  |  ###  |
| #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |
| #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |
| #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |
|       |       |  ###  |  ###  |  ###  |  ###  |  ###  |       |  ###  |  ###  |
| #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |
| #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |
| #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |
|  ###  |       |  ###  |  ###  |       |  ###  |  ###  |       |  ###  |  ###  |
```
If the number is smaller than 6 digits, the result should be justified to the right, with the unused segments being blank (as they are not turned on). Refer to the sample test for an example.

**Note:** There should not be any trailing whitespace for any line.

Please rate and enjoy!
"""

from itertools import chain

nums = """\
       |  ###  |       |  ###  |  ###  |       |  ###  |  ###  |  ###  |  ###  |  ###  |
       | #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |
       | #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |
       | #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |
       |       |       |  ###  |  ###  |  ###  |  ###  |  ###  |       |  ###  |  ###  |
       | #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |
       | #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |
       | #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |
       |  ###  |       |  ###  |  ###  |       |  ###  |  ###  |       |  ###  |  ###  |
"""
nums = nums.splitlines()
chunks = [[line[i:i+8] for line in nums] for i in range(0, len(nums[0]), 8)]
d = dict(zip(' 0123456789', chunks))

def segment_display(num):
    nums_s = tuple(d[n] for n in f'{num:>6}')
    return '\n'.join('|' + ''.join(row) for row in zip(*nums_s))
