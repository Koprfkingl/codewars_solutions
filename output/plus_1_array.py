"""Kata - +1 Array

completed at: 2022-12-20 13:16:59
by: Jakub Červinka

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

- the array can't be empty
- only non-negative, single digit integers are allowed

Return `nil` (or your language's equivalent) for invalid inputs.

### Examples

**Valid arrays**

`[4, 3, 2, 5]` would return `[4, 3, 2, 6]`  
`[1, 2, 3, 9]` would return `[1, 2, 4, 0]`  
`[9, 9, 9, 9]` would return `[1, 0, 0, 0, 0]`  
`[0, 1, 3, 7]` would return `[0, 1, 3, 8]`

**Invalid arrays**

`[1, -9]` is invalid because `-9` is **not a non-negative integer**

`[1, 2, 33]` is invalid because `33` is **not a single-digit integer**




"""

def up_array(arr):
    if not arr:
        return
    if not all(0 <= num <= 9 for num in arr):
        return
    the_num = int(''.join(map(str, arr))) + 1
    the_str = str(the_num).zfill(len(arr))
    return list(map(int, the_str))    
