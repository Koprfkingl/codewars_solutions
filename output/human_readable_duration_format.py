"""Kata - Human readable duration format

completed at: 2019-02-21 19:53:29
by: Jakub Červinka

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns `"now"`. Otherwise,  the duration is expressed as a combination of `years`, `days`, `hours`, `minutes` and `seconds`.

It is much easier to understand with an example:

```text
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
```

**For the purpose of this Kata, a year is 365 days and a day is 24 hours.**

Note that spaces are important.


### Detailed rules

The resulting expression is made of components like `4 seconds`, `1 year`, etc.  In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (`", "`). Except the last component, which is separated by `" and "`, just like it would be written in English. 

A more significant units of time will occur before than a least significant one. Therefore, `1 second and 1 year` is not correct, but `1 year and 1 second` is.

Different components have different unit of times. So there is not repeated units like in `5 seconds and 1 second`.

A component will not appear at all if its value happens to be zero.  Hence, `1 minute and 0 seconds` is not valid, but it should be just `1 minute`.

 A unit of time must be used "as much as possible". It means that the function should not return `61 seconds`, but `1 minute and 1 second` instead.  Formally, the duration specified by  of a component must not be greater than any valid more significant unit of time.

"""

def format_duration(seconds):
    intervals = (
    ('years', 31536000),
    #('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
    )
    
    if not seconds: return 'now'
    
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    if len(result) == 1:
        return result[0]
    return ', '.join(result[:-1]) + ' and ' + str(result[-1])
