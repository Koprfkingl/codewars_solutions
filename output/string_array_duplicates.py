"""Kata - String  array duplicates

completed at: 2023-05-01 16:32:46
by: Jakub Červinka

In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example: 

  * `dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"]`. 
  
  * `dup(["kelless","keenness"]) = ["keles","kenes"]`.

Strings will be lowercase only, no spaces. See test cases for more examples.

~~~if:rust
For the sake of simplicity you can use the macro 'vec_of_strings!' to create a Vec<String> with an array of string literals.
~~~

Good luck!

If you like this Kata, please try:

[Alternate capitalization](https://www.codewars.com/kata/59cfc000aeb2844d16000075)

[Vowel consonant lexicon](https://www.codewars.com/kata/59cf8bed1a68b75ffb000026)
"""

from itertools import groupby
import operator

def dup(arry):
    return [
        ''.join(map(next, map(operator.itemgetter(1), groupby(iterable, None))))
        for iterable in arry
    ]
