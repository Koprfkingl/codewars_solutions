"""Kata - Difference of 2

completed at: 2023-05-09 07:45:39
by: Jakub Červinka

The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

The result array should be sorted in ascending order of values.

Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.


## Examples
~~~if-not:python,julia
```
[1, 2, 3, 4]  should return [[1, 3], [2, 4]]

[4, 1, 2, 3]  should also return [[1, 3], [2, 4]]

[1, 23, 3, 4, 7] should return [[1, 3]]

[4, 3, 1, 5, 6] should return [[1, 3], [3, 5], [4, 6]]
```
~~~
~~~if:python,julia
```
[1, 2, 3, 4]  should return [(1, 3), (2, 4)]

[4, 1, 2, 3]  should also return [(1, 3), (2, 4)]

[1, 23, 3, 4, 7] should return [(1, 3)]

[4, 3, 1, 5, 6] should return [(1, 3), (3, 5), (4, 6)]
```
~~~

"""

def twos_difference(lst): 
    lst.sort()
    return [
        (e, e + 2)
        for i, e in enumerate(lst)
        if e + 2 in lst[-len(lst) + i:]
    ]
