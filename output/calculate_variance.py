"""Kata - Calculate Variance

completed at: 2023-05-30 13:13:35
by: Jakub Červinka

Write a function which will accept a sequence of numbers and calculate the variance for the sequence.

The variance for a set of numbers is found by subtracting the mean from every value, squaring the results, adding them all up and dividing by the number of elements.

For example, in pseudo code, to calculate the variance for `[1, 2, 2, 3]`.
```
mean = (1 + 2 + 2 + 3) / 4
=> 2

variance = ((1 - 2)^2 + (2 - 2)^2 + (2-2)^2 + (3 - 2)^2)  /  4
=> 0.5
```

```if:javascript,coffeescript
The results are tested after being rounded to 4 decimal places using Javascript's toFixed method.
```
```if:cobol,haskell
Results are tested to a relative error of `1e-8`.
```
```if:python
Results are tested to a relative error of `1e-4`.
```

"""

from statistics import pvariance as variance
