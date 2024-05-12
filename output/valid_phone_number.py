"""Kata - Valid Phone Number

completed at: 2019-03-27 09:51:39
by: Jakub Červinka

Write a function that accepts a string, and returns true if it is in the form of a phone number. <br/>Assume that any integer from 0-9 in any of the spots will produce a valid phone number.<br/>

Only worry about the following format:<br/>
(123) 456-7890   (don't forget the space after the close parentheses) <br/> <br/>
Examples:

```
"(123) 456-7890"  => true
"(1111)555 2345"  => false
"(098) 123 4567"  => false
```

"""

def validPhoneNumber(phoneNumber):
    import re
    return bool(re.findall(r'^\(\d{3}\) \d{3}-\d{4}$', phoneNumber))
