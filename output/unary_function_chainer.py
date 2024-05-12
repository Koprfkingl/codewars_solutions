"""Kata - Unary function chainer

completed at: 2023-02-02 20:12:58
by: Jakub Červinka

Your task is to write a higher order function for chaining together
a list of unary functions. In other words, it should return a function
that does a left fold on the given functions.

```python
chained([a,b,c,d])(input)
```
Should yield the same result as
```python
d(c(b(a(input))))
```
"""

def chained(functions):
    def func(arg):
        result = arg
        for f in functions:
            result = f(result)
        return result
    return func
