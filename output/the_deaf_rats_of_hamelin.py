"""Kata - The Deaf Rats of Hamelin

completed at: 2023-06-01 20:22:56
by: Jakub Červinka

<img src="https://i.imgur.com/ta6gv1i.png?1"/>

---

# Story

The <a href="https://en.wikipedia.org/wiki/Pied_Piper_of_Hamelin">Pied Piper</a> has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

# Kata Task

How many deaf rats are there?

# Legend

* ```P``` = The Pied Piper
* ```O~``` = Rat going left
* ```~O``` = Rat going right

# Example

* ex1 ```~O~O~O~O P``` has 0 deaf rats


* ex2 ```P O~ O~ ~O O~``` has 1 deaf rat


* ex3 ```~O~O~O~OP~O~OO~``` has 2 deaf rats

---

# Series

* [The deaf rats of Hamelin (2D)](https://www.codewars.com/kata/the-deaf-rats-of-hamelin-2d)
</span>
"""

from itertools import islice

def count_deaf_rats(town):
    left, piper, right = town.partition('P')
    left = left.replace(' ', '')
    right = right.replace(' ', '')

    def batched(iterable):
        it = iter(iterable)
        while batch := tuple(islice(it, 2)):
            yield ''.join(batch)

    deaf = 0
    deaf += sum(rat == 'O~' for rat in batched(left))
    deaf += sum(rat == '~O' for rat in batched(right))

    return deaf
