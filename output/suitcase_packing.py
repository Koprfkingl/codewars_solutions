"""Kata - Suitcase packing

completed at: 2019-02-24 19:48:30
by: Jakub Červinka

Mr. Square is going on a holiday. He wants to bring 2 of his favorite squares with him, so he put them in his rectangle suitcase.

Write a function that, given the size of the squares and the suitcase, return whether the squares can fit inside the suitcase.
```Python
fit_in(a,b,m,n)
a,b are the sizes of the 2 squares
m,n are the sizes of the suitcase
```

# Example
```Python
fit_in(1,2,3,2) should return True
fit_in(1,2,2,1) should return False
fit_in(3,2,3,2) should return False
fit_in(1,2,1,2) should return False
```

"""

def fit_in(a,b,m,n):
    return a + b <= m and max(a, b) <= n or a + b <= n and max(a, b) <= m
