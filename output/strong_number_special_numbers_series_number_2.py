"""Kata - Strong Number (Special Numbers Series #2)  

completed at: 2019-11-05 13:49:31
by: 

Strong number is a number with the sum of the factorial of its digits is equal to the number itself.

For example, 145 is strong, because `1! + 4! + 5! = 1 + 24 + 120 = 145`.

### Task

Given a positive number, find if it is strong or not, and return either `"STRONG!!!!"` or `"Not Strong !!"`.

### Examples

- `1` is a strong number, because `1! = 1`, so return `"STRONG!!!!"`.
- `123` is not a strong number, because `1! + 2! + 3! = 9` is not equal to 123, so return `"Not Strong !!"`.
- `145` is a strong number, because `1! + 4! + 5! = 1 + 24 + 120 = 145`, so return `"STRONG!!!!"`.
- `150` is not a strong number, because `1! + 5! + 0! = 122` is not equal to 150, so return `"Not Strong !!"`.

___

[Playing with Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

[Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

[For More Enjoyable Katas](http://www.codewars.com/users/MrZizoScream/authored)

"""

from math import factorial
def strong_num(number):
    splitted = list(map(int, str(number)))
    resultComputation = 0
    for num in splitted:
        resultComputation += factorial(num)
    if resultComputation == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
