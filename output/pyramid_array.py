"""Kata - Pyramid Array

completed at: 2022-09-19 18:51:05
by: Jakub Červinka

Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

```
pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
```

**Note:** the subarrays should be filled with `1`s

```if:c
Subarrays should not overlap; this will be tested.
Do not forget to de-allocate memory in `free_pyramid()`, this will be tested as well.
```

"""

def pyramid(n):
    return [[1] * i for i in range(1, n + 1)]
