"""Kata - CamelCase Method

completed at: 2019-04-19 17:11:08
by: Jakub Červinka

Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

#### Examples (input --> output):

```
"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"
```

Don't forget to rate this kata! Thanks :)

"""

def camel_case(string):
    return string.title().replace(' ','')
