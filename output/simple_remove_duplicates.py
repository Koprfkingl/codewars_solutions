"""Kata - Simple remove duplicates

completed at: 2020-07-23 07:18:14
by: 

Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

### Example:

For input: `[3, 4, 4, 3, 6, 3]`

* remove the `3` at index `0`
* remove the `4` at index `1`
* remove the `3` at index `3`

Expected output: `[4, 6, 3]`

More examples can be found in the test cases. 

Good luck!
"""

def solve(arr):
    to_delete_indeces = []
    for i in range(0, len(arr)):
        if arr[i] in arr[i+1:]:
            to_delete_indeces.append(i)
    print(to_delete_indeces)

    offset = 0
    for index in to_delete_indeces:
        del arr[index-offset]
        offset += 1
    print(arr)

    return arr

