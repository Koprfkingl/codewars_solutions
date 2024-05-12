"""Kata - Build Tower

completed at: 2019-04-10 10:00:56
by: Jakub Červinka

Build Tower
---

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer `number of floors`. A tower block is represented with `"*"` character.

For example, a tower with `3` floors looks like this:

```
[
  "  *  ",
  " *** ", 
  "*****"
]
```

And a tower with `6` floors looks like this:

```
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```

___

Go challenge [Build Tower Advanced](https://www.codewars.com/kata/57675f3dedc6f728ee000256) once you have finished this :)

"""

def tower_builder(f):
    return ['{:^{}}'.format('*'*(n*2+1), f*2-1) for n in range(f)]
