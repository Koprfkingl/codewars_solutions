"""Kata - Kebabize

completed at: 2019-05-29 11:20:15
by: Jakub Červinka

Modify the `kebabize` function so that it converts a camel case string into a kebab case.


```
"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
```

Notes:
  - the returned string should only contain lowercase letters
"""

def kebabize(string):
    import re
    no_numbers = re.sub(r'\d','',string)
    return re.sub(r'(?=\B([A-Z]))','-',no_numbers).lower()
