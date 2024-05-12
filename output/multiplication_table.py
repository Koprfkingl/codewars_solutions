"""Kata - Multiplication table

completed at: 2022-03-24 20:29:01
by: Jakub Červinka

Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given `size` is 3:
```
1 2 3
2 4 6
3 6 9
```

For the given example, the return value should be: 

```js
[[1,2,3],[2,4,6],[3,6,9]]
```
```julia
[1 2 3; 2 4 6; 3 6 9]
```

```if:c
Note: in C, you must return an allocated table of allocated rows
```

"""

def multiplication_table(s):
    return [list(range(m, m * s + 1, m)) for m in range(1, s + 1)]
