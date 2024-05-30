"""Kata - Stringy Strings

completed at: 2019-08-28 08:54:00
by: 

write me a function `stringy` that takes a `size` and returns a `string` of alternating `1`s and `0`s.

the string should start with a `1`.

a string with `size` 6 should return :`'101010'`.

with `size` 4 should return : `'1010'`.

with `size` 12 should return : `'101010101010'`.

The size will always be positive and will only use whole numbers.


"""

def stringy(size):
    # Good Luck!
    string_even = '10'
    string1 = '1'
    if size%2 == 0:
        output = size//2 * string_even
    else:
        output = (size//2*string_even)+string1

    return output
