"""Kata - Convert number to reversed array of digits

completed at: 2024-03-23 13:00:20
by: Jakub Červinka

# Convert number to reversed array of digits

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

## Example(Input => Output):

```
35231 => [1,3,2,5,3]
0 => [0]
```

"""

def digitize(n):
    text = str(n)
    vysledek = []
    for cislo in text:
        vysledek.append(int(cislo))
    vysledek.reverse()
    return vysledek
