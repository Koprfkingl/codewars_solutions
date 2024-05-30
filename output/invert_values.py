"""Kata - Invert values

completed at: 2019-09-13 14:38:15
by: 

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
```

```if:javascript,python,ruby,php,elixir,dart,go,lua
You can assume that all values are integers. Do not mutate the input array.
```

```if:c,riscv
### Notes:
- All values are greater than `INT_MIN`
- The input should be modified, not returned.
```

~~~if:riscv
RISC-V: The function signature is:

```c
void invert(int *arr, size_t size);
```

The input array is `arr` which contains `size` elements. Mutate the array in-place according to the above specification. You do not need to return anything.
~~~

"""

def invert(lst):
    inv = []
    for i in lst:
        if i >= 0:
            inv.append(-i)

        else:
            inv.append(abs(i))
    return inv
