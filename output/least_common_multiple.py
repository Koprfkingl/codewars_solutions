"""Kata - Least Common Multiple

completed at: 2023-05-04 11:42:48
by: Jakub Červinka

Write a function that calculates the *least common multiple* of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return `1`. If any argument is `0`, return `0`.

~~~if:objc,c
NOTE: The first (and only named) argument of the function `n` specifies the number of arguments in the variable-argument list. Do **not** take `n` into account when computing the LCM of the numbers.
~~~

~~~if:lambdacalc
### Encodings

`purity: LetRec`  
`numEncoding: BinaryScott`  
export constructors `nil, cons` for your `List` encoding  
~~~

"""

from math import lcm
