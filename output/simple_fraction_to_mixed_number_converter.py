"""Kata - Simple fraction to mixed number converter

completed at: 2022-10-17 08:51:18
by: Jakub Červinka

# Task
Given a string representing a simple fraction `x/y`, your function must return a string representing the corresponding [mixed fraction](http://en.wikipedia.org/wiki/Fraction_%28mathematics%29#Mixed_numbers) in the following format:

```[sign]a b/c```

where `a` is integer part and `b/c` is irreducible proper fraction. There must be exactly one space between `a` and `b/c`. Provide `[sign]` only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

If the `x/y` equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).

# Value ranges

* -10 000 000 < ```x``` < 10 000 000
* -10 000 000 < ```y``` < 10 000 000

# Examples

* Input: `42/9`, expected result: `4 2/3`.
* Input: `6/3`, expedted result: `2`.
* Input: `4/6`, expected result: `2/3`.
* Input: `0/18891`, expected result: `0`.
* Input: `-10/7`, expected result: `-1 3/7`.
* Inputs `0/0` or `3/0` must raise a zero division error.

# Note
Make sure not to modify the input of your function in-place, it is a bad practice.
"""

from fractions import Fraction

def mixed_fraction(s):
    # store the sign
    sign = '' if s.count('-') % 2 == 0 else '-'
    # make string positive
    s = s.replace('-', '')
    # prepare fraction
    frac = Fraction(s)
    # take multiple and simplify names
    multiple, new_num, den = *divmod(frac.numerator, frac.denominator), frac.denominator
    
    res = None
    match multiple, new_num, den:
        case m, 0, _:
            res = str(m)
        case 0, n, d:
            res = f'{n}/{d}'
        case _:
            res = f'{multiple} {new_num}/{den}'
    if sign and res != '0':
        res = sign + res
    return res
