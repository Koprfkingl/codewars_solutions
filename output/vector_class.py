"""Kata - Vector class

completed at: 2023-06-15 14:28:45
by: Jakub Červinka

Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

```coffeescript
a = new Vector([1, 2, 3])
b = new Vector([3, 4, 5])
c = new Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # throws an error
```
```javascript
var a = new Vector([1, 2, 3]);
var b = new Vector([3, 4, 5]);
var c = new Vector([5, 6, 7, 8]);

a.add(b);      // should return a new Vector([4, 6, 8])
a.subtract(b); // should return a new Vector([-2, -2, -2])
a.dot(b);      // should return 1*3 + 2*4 + 3*5 = 26
a.norm();      // should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c);      // throws an error
```
```python
a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
```

If you try to add, subtract, or dot two vectors with different lengths, ***you must throw an error***!

Also provide:

- a `toString` method, so that using the vectors from above, `a.toString() === '(1,2,3)'` (in Python, this is a `__str__` method, so that `str(a) == '(1,2,3)'`)
- an `equals` method, to check that two vectors that have the same components are equal

**Note:** the test cases will utilize the user-provided `equals` method.
"""

from dataclasses import dataclass
import itertools

@dataclass
class Vector:
    coords: list

    def check_size(func):
        def wrapper(this, other, *args, **kwargs):
            if len(this.coords) != len(other.coords):
                print('ValueError')
            return func(this, other, *args, **kwargs)
        return wrapper
    
    @check_size
    def equals(self, other):
        return self.coords == other.coords
    
    @check_size
    def add(self, other):
        return Vector([a + b for a, b in zip(self.coords, other.coords)])
    
    @check_size
    def subtract(self, other):
        return Vector([a - b for a, b in zip(self.coords, other.coords)])
    
    @check_size
    def dot(self, other):
        return sum(a * b for a, b in zip(self.coords, other.coords))
    
    def norm(self):
        return sum(a ** 2 for a in self.coords) ** 0.5
    
    def __str__(self):
        return str(tuple(self.coords)).replace(' ', '')
