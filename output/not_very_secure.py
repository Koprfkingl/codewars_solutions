"""Kata - Not very secure

completed at: 2020-11-14 23:07:33
by: Jakub Červinka

In this example you have to validate if a user input string is alphanumeric. The given string is not `nil/null/NULL/None`, so you don't have to check that.

The string has the following conditions to be alphanumeric:

* At least one character (`""` is not valid)
* Allowed characters are uppercase / lowercase latin letters and digits from `0` to `9`
* No whitespaces / underscore

"""

def alphanumeric(password):
    import re
    pattern = re.compile(r'\w+')
    matches = re.fullmatch(pattern, password)
    return bool(matches)
