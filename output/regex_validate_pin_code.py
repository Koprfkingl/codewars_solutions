"""Kata - Regex validate PIN code

completed at: 2023-05-30 09:37:59
by: Jakub Červinka

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but **exactly** 4 digits or exactly 6 digits. 

If the function is passed a valid PIN string, return `true`, else return `false`.

## Examples (**Input --> Output)**
```
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
```

"""

import re
def validate_pin(pin):
    return bool(re.fullmatch(r'\d{4}|\d{6}', pin))
