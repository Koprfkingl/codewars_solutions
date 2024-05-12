"""Kata - How many are smaller than me?

completed at: 2024-01-21 20:21:09
by: Jakub Červinka

Write a function that given, an array ```arr```, returns an array containing at each index ```i``` the amount of numbers that are smaller than ```arr[i]``` to the right.

For example:

```
* Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
* Input [1, 2, 0] => Output [1, 1, 0]
```

If you've completed this one and you feel like testing your performance tuning of this same kata, head over to the much tougher version <a href = 'http://www.codewars.com/kata/56a1c63f3bc6827e13000006'>How many are smaller than me II?</a>

"""

def smaller(arr):
    return [
        sum(c < arr[i] for c in arr[i + 1:])
        for i in range(len(arr))
    ]
