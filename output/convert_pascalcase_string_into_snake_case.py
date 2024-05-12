"""Kata - Convert PascalCase string into snake_case

completed at: 2019-04-23 13:17:48
by: Jakub Červinka

Complete the function/method so that it takes a `PascalCase` string and returns the string in `snake_case` notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

## Examples
```
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
```
"""

def to_underscore(strng):
    import re
    if isinstance(strng, int): return str(strng)
    return re.sub(r'([A-Z][a-z\d]+)', r'_\1', strng)[1:].lower()
    
    
