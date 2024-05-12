"""Kata - Valid Braces

completed at: 2019-04-15 11:01:48
by: Jakub Červinka

Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return `true` if the string is valid, and `false` if it's invalid.


This Kata is similar to the [Valid Parentheses](https://www.codewars.com/kata/valid-parentheses-1) Kata, but introduces new characters: brackets `[]`, and curly braces `{}`. Thanks to `@arnedag` for the idea!


All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: `()[]{}`. 



### What is considered Valid?


A string of braces is considered valid if all braces are matched with the correct brace.


## Examples

```
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
```


"""

def validBraces(string):
    
    # odd list cant be balanced
    if len(string) % 2 == 1:
        return False
        
    stack = []
    par_dict = {"(": ")", "{": "}", "[": "]"}
    
    for par in string:
        if par in par_dict:
            stack.append(par)
        elif not stack or par_dict[stack.pop()] is not par:
            return False
    return not stack
