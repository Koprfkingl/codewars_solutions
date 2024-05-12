"""Kata - Calculating with Functions

completed at: 2023-06-14 11:56:03
by: Jakub Červinka

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

```javascript
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
```
```haskell
seven $ times $ five   ->  35 :: Int
four $ plus $ nine     ->  13 :: Int
eight $ minus $ three  ->   5 :: Int
six $ dividedBy $ two  ->   3 :: Int
```
```ruby
seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3
```
```python
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
```
```factor
seven multiplied-by five   ! must evaluate to 35
four plus nine             ! must evaluate to 13
eight minus three          ! must evaluate to 5
six divided-by two         ! must evaluate to 3
```

Requirements:
~~~if:ruby,python
* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:
~~~
~~~if:factor
* There must be a word for each number from 0 ("zero") to 9 ("nine")
* There must be a word for each of the following mathematical operations: plus, minus, multiplied-by, divided-by
* Each calculation consist of exactly one operation and two numbers
* The leftmost word represents the left operand, the rightmost word represents the right operand
* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:
~~~
~~~if-not:ruby,python,factor
* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:
~~~

```javascript
eight(dividedBy(three()));
```
```haskell
eight $ dividedBy $ three
```
```ruby
eight(divided_by(three))
```
```python
eight(divided_by(three()))
```
```factor
eight divided-by three
```
"""

def zero(f=None): return f(0) if f else 0
def one(f=None): return f(1) if f else 1
def two(f=None): return f(2) if f else 2
def three(f=None): return f(3) if f else 3
def four(f=None): return f(4) if f else 4
def five(f=None): return f(5) if f else 5
def six(f=None): return f(6) if f else 6
def seven(f=None): return f(7) if f else 7
def eight(f=None): return f(8) if f else 8
def nine(f=None): return f(9) if f else 9


def plus(x): return lambda y: y + x
def minus(x): return lambda y: y - x
def times(x): return lambda y: y * x
def divided_by(x): return lambda y: y // x

