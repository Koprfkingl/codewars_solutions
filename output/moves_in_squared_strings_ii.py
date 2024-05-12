"""Kata - Moves in squared strings (II)

completed at: 2023-08-22 11:18:40
by: Jakub Červinka

You are given a string of `n` lines, each substring being `n` characters long: For example:

`s = "abcd\nefgh\nijkl\nmnop"`

We will study some transformations of this square of strings.

- Clock rotation 180 degrees: rot
```
rot(s) => "ponm\nlkji\nhgfe\ndcba"
```
- selfie_and_rot(s) (or selfieAndRot or selfie-and-rot)
It is initial string + string obtained by clock rotation 180 degrees with dots interspersed in order (hopefully) to better show the rotation when printed.
```
s = "abcd\nefgh\nijkl\nmnop" --> 
"abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
```
or printed:

```
|rotation        |selfie_and_rot
|abcd --> ponm   |abcd --> abcd....
|efgh     lkji   |efgh     efgh....
|ijkl     hgfe   |ijkl     ijkl....   
|mnop     dcba   |mnop     mnop....
                           ....ponm
                           ....lkji
                           ....hgfe
                           ....dcba
```
Notice that the *number of dots* is the *common length* of "abcd", "efgh", "ijkl", "mnop".

#### Task:
- Write these two functions `rot`and `selfie_and_rot`

and

- high-order function `oper(fct, s)` where

 - fct is the function of one variable f to apply to the string `s`
(fct will be one of `rot, selfie_and_rot`)

#### Examples:
```
s = "abcd\nefgh\nijkl\nmnop"
oper(rot, s) => "ponm\nlkji\nhgfe\ndcba"
oper(selfie_and_rot, s) => "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
```
#### Notes:
- The form of the parameter `fct` in oper
changes according to the language. You can see each form according to the language in "Your test cases".
- It could be easier to take these katas from number (I) to number (IV)

Forthcoming katas will study other tranformations.

####  Bash Note:
The input strings are separated by `,` instead of `\n`. The ouput strings should be separated by `\r` instead of `\n`. See "Sample Tests".
"""

def rot(s):
    return '\n'.join(
        ''.join(row[::-1])
        for row in s.split('\n')[::-1]
    )
    
def selfie_and_rot(s):
    l = len(s.split('\n')[0]) * 2
    res = []
    for r in s.split('\n'):
        res.append(f'{r:.<{l}}')
    for r in rot(s).split('\n'):
        res.append(f'{r:.>{l}}')
    return '\n'.join(res)

def oper(fct, s):
    return fct(s)
