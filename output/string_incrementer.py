"""Kata - String incrementer

completed at: 2019-04-22 16:04:36
by: Jakub Červinka

Your job is to write a function which increments a string, to create a new string.

- If the string already ends with a number, the number should be incremented by 1.
- If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

`foo -> foo1`

`foobar23 -> foobar24`

`foo0042 -> foo0043`

`foo9 -> foo10`

`foo099 -> foo100`

*Attention: If the number has leading zeros the amount of digits should be considered.*

"""

def increment_string(strng):
    import re
    
    text, *number = re.split(r'(\d+)$', strng)[:2]

    if not number:
        return text + '1'
    else:
        align = len(number[0])
        added = int(number[0]) + 1
        return '{}{}'.format(text, str(added).zfill(align))

