"""Kata - Primorial Of  a Number 

completed at: 2023-05-09 11:59:35
by: Jakub Červinka

# Definition (Primorial Of a Number)

*Is similar to factorial of a number*, **_In primorial_**, not all the natural numbers get multiplied, **_only prime numbers are multiplied to calculate the primorial of a number_**. It's denoted with **_P_**<sub>**_#_**</sub> and it is the product of the first n prime numbers.
___ 

# Task

**_Given_** *a number N* , **_calculate its primorial_**. ![!alt](https://i.imgur.com/mdX8dJP.png)  ![!alt](https://i.imgur.com/mdX8dJP.png)  
___

# Notes

* **_Only positive_** numbers *will be passed (N > 0)* .
___

# Input >> Output Examples:

``` cpp
1- numPrimorial (3) ==> return (30)
```
```prolog
1 - num_primorial(3, 30).
```
```rust
1 - num_primorial(3) // 30
```
```clojure
1 - (num-primorial 3) ;; 30
```

## **_Explanation_**:

**_Since_** *the passed number is (3)* ,**_Then_** **_the primorial_** *should obtained by multiplying*  ```2 * 3 * 5 = 30 .```

### Mathematically written as , **_P_**<sub>3</sub>**_#_** = 30 .
___ 

```cpp
2- numPrimorial (5) ==> return (2310)
```
```prolog
2 - num_primorial(5, 2310).
```
```rust
2 - num_primorial(5) // 2310
```
```clojure
2 - (num-primorial 5) ;; 2310
```

## **_Explanation_**:


**_Since_** *the passed number is (5)* ,**_Then_** **_the primorial_** *should obtained by multiplying*  ``` 2 * 3 * 5 * 7 * 11 = 2310 .```

### Mathematically written as , **_P_**<sub>5</sub>**_#_** = 2310 .
___

```cpp
3- numPrimorial (6) ==> return (30030)
```
```prolog
3 - num_primorial(6, 30030).
```
```rust
3 - num_primorial(6) // 30030
```
```clojure
3 - (num-primorial 6) ;; 30030
```

## **_Explanation_**: 

**_Since_** *the passed number is (6)* ,**_Then_** **_the primorial_** *should obtained by multiplying*  ``` 2 * 3 * 5 * 7 * 11 * 13 = 30030 .```

### Mathematically written as , **_P_**<sub>6</sub>**_#_** = 30030 .
___
___
___

# [Playing with Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

# [Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

# [For More Enjoyable Katas](http://www.codewars.com/users/MrZizoScream/authored)
___

## ALL translations are welcomed

## Enjoy Learning !!
# Zizou

"""

def genPrimes():
    yield 2                      # get the first prime out of the way
    skips      = dict()          # multiples to skip {Multiple:2xPrime}
    multiples  = ((p*p,2*p) for p in genPrimes()) # multiples of primes
    skipMark,_ = next(multiples)                  # skipping coverage
    N = 1                        # prime candidate (odd numbers)
    while True:
       N += 2                        # next prime candidate
       if N >= skipMark:                     # extend skips coverage
           skipMark,stride = next(multiples) # 1st multiple and stride
           skips[skipMark] = stride          
       if N in skips:                # not a prime (multiple of a prime)   
           stride   = skips.pop(N)   # get prime multiple steps
           multiple = N + stride     # advance skip to next multiple
           while multiple in skips:
               multiple += stride    # not already skipped
           skips[multiple] = stride
       else:                         # N is prime
           yield N                   # return it 

from itertools import islice
from functools import reduce
from operator import mul
            
def num_primorial(n):
    return reduce(mul, islice(genPrimes(), n))
    
