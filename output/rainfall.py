"""Kata - Rainfall

completed at: 2019-03-04 20:06:47
by: Jakub Červinka

`data`and `data1` are two strings with rainfall records of a few cities for months from January to December.
The records of towns are separated by `\n`. The name of each town is followed by `:`. 

`data` and `towns` can be seen in "Your Test Cases:".

#### Task:
- function: `mean(town, strng)` should return the average of rainfall for the city `town` and the `strng` `data` or `data1` (In R and Julia this function is called `avg`).
- function: `variance(town, strng)` should return the variance of rainfall for the city `town` and the `strng` `data` or `data1`.

#### Examples:

```
mean("London", data), 51.19(9999999999996) 
variance("London", data), 57.42(833333333374)
```

#### Notes:
- if functions `mean` or `variance` have as parameter `town` a city which has no records return `-1` or `-1.0` (depending on the language)

    
- Don't truncate or round: the tests will pass if `abs(your_result - test_result) <= 1e-2`
or `abs((your_result - test_result) / test_result) <= 1e-6` depending on the language.


- Shell
  1) Shell tests only variance.
  2) In "function "variance" $1 is "data", $2 is "town".

    
- A ref: <http://www.mathsisfun.com/data/standard-deviation.html>


- `data` and `data1` (can be named `d0` and `d1` depending on the language; see "Sample Tests:") are adapted from:  <http://www.worldclimate.com>

"""

import numpy as np

def mean(town, data):
    rain = {}
    try:
        for line in data.split('\n'):
        
            key, months_str = line.split(':')
            values = []
            for month in months_str.split(','):
                values.append(float(month.split(' ')[1]))
            rain[key] = values
        
        return np.mean(rain[town])
    except Exception as e:
        return -1
            
def variance(town, data):
    rain = {}
    try:
        for line in data.split('\n'):
        
            key, months_str = line.split(':')
            values = []
            for month in months_str.split(','):
                values.append(float(month.split(' ')[1]))
            rain[key] = values
        
        return np.var(rain[town])
    except Exception as e:
        return -1
