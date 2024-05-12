"""Kata - Transform To Prime

completed at: 2023-09-04 19:18:32
by: Jakub Červinka

# Task : 

**_Given_** *a List [] of n integers* , **_find minimum number_** to be **inserted** in a *list*, so that **_sum of all elements of list_** should *equal the closest prime number* .
___
# Notes

* **_List size_** is *at least 2* .

* **_List's numbers_** will only **_positives_** (n > 0) .

* **_Repetition_** of numbers in the list **_could occur_** .

* **_The newer list's sum_** should *equal the closest prime number* . 
___

# Input >> Output Examples

```cpp
1- minimumNumber ({3,1,2}) ==> return (1)
```
## **_Explanation_**:

* **_Since_** , **the sum** of the list's elements equal to **_(6)_** , *the minimum number to be inserted to transform the sum to prime number* is **_(1)_** , *which will make **_the sum of the List_** equal the closest prime number **_(7)_*** .
___

```cpp
2-  minimumNumber ({2,12,8,4,6}) ==> return (5)
```
## **_Explanation_**: 

* **_Since_** , **the sum** of the list's elements equal to **_(32)_** , *the minimum number to be inserted to transform the sum to prime number* is **_(5)_** , *which will make **_the sum of the List_** equal the closest prime number **_(37)_*** .
___

```cpp
3- minimumNumber ({50,39,49,6,17,28}) ==> return (2)
```
## **_Explanation_**: 

* **_Since_** , **the sum** of the list's elements equal to **_(189)_** , *the minimum number to be inserted to transform the sum to prime number* is **_(2)_** , *which will make **_the sum of the List_** equal the closest prime number **_(191)_*** .
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

from itertools import count

def is_prime(x):
    p, inc = 2, 1
    while p * p <= x:
        if x % p == 0:
            return False
        p, inc = p + inc, 2
    return x > 1

def minimum_number(in_list):
    s = sum(in_list)
    for num in count(start=s):
        if is_prime(num):
            return num - s
