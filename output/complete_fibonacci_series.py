"""Kata - Complete Fibonacci Series

completed at: 2023-06-22 12:32:24
by: Jakub Červinka

The function 'fibonacci' should return an array of fibonacci numbers.  The function takes a number as an argument to decide how many no. of elements to produce. If the argument is less than or equal to 0 then return empty array

Example:
```javascript
fibonacci(4) // should return  [0,1,1,2]
fibonacci(-1) // should return []
```
```ruby
fibonacci(4); # should return  [0,1,1,2]
fibonacci(-1); # should return []
```
```python
fibonacci(4) # should return  [0,1,1,2]
fibonacci(-1) # should return []
```


"""

def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
