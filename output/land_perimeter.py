"""Kata - Land perimeter

completed at: 2023-05-04 14:24:01
by: Jakub Červinka

Given an array `arr` of strings, complete the function by calculating the total perimeter of all the islands. Each piece of land will be marked with `'X'` while the water fields are represented as `'O'`. Consider each tile being a perfect `1 x 1` piece of land. Some examples for better visualization:

```text
['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO'] 
```

which represents:
![](https://i.snag.gy/ZOQYs2.jpg)

should return: `"Total land perimeter: 24"`.

Following input:

```text
['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']
```

which represents:
![](https://i.snag.gy/Kv9BEz.jpg)

should return: `"Total land perimeter: 18"`
"""

def land_perimeter(arr):
    land = {
        (x, y)
        for y, row in enumerate(arr)
        for x, v in enumerate(row)
        if v == 'X'
    }
    dirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    perimeter = sum(
        (x + dx, y + dy) not in land
        for (x, y) in land
        for dx, dy in dirs
    )
    return f'Total land perimeter: {perimeter}'
            
