"""Kata - Valid Parentheses

completed at: 2019-03-07 14:23:24
by: Jakub Červinka

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return `true` if the string is valid, and `false` if it's invalid.

## Examples

```
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```

## Constraints

`0 <= input.length <= 100`

~~~if-not:javascript,go,cobol
Along with opening (`(`) and closing (`)`) parenthesis, input may contain any valid ASCII characters.  Furthermore, the input string may be empty and/or not contain any parentheses at all.  Do **not** treat other forms of brackets as parentheses (e.g. `[]`, `{}`, `<>`).
~~~

"""

def valid_parentheses(string):
    pars = list(filter(lambda c: c in '()', string))
    stack = []
    if len(pars) == 0: return True
    else:
        for p in pars:
            if p == ')' and '(' not in stack: return False
            if p == '(': stack.append(p)
            if p == ')' and stack and stack[-1] == '(': stack.pop()
    return not stack
