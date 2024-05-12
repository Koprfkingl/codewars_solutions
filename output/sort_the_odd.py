"""Kata - Sort the odd

completed at: 2019-04-15 11:43:32
by: Jakub Červinka

## Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

### Examples

```
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```

~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` and deconstructor `foldl` for your `List` encoding  
~~~
"""

def sort_array(source_array):
    result = []
    to_return = []
    for i, v in enumerate(source_array):
        if v % 2 == 0:
            to_return.append((i, v))
        else:
            result.append(v)
    result.sort()
    for even in to_return:
        result.insert(*even)
    
    return result
    
