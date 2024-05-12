"""Kata - Dashatize it

completed at: 2019-05-09 11:37:15
by: Jakub Červinka

Given an integer, return a string with dash `'-'` marks before and after each odd digit, but do not begin or end the string with a dash mark.


Ex:
```javascript
274 -> '2-7-4'
6815 -> '68-1-5'
```
"""

def dashatize(num):
    if num:
        string = str(abs(num))
        pre_string = ''.join([f'-{ch}-' if int(ch) % 2 == 1 else ch for ch in string])
        truncated = pre_string.replace('--', '-').strip('-')
        return truncated
    else:
        return str(num)
    
    
    
