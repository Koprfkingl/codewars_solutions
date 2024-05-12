"""Kata - Double Char

completed at: 2022-03-07 16:29:17
by: Jakub Červinka

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

### Examples (Input -> Output):
```
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
```
Good Luck!

~~~if:riscv
RISC-V: The function signature is

```c
char *double_char(const char *string, char *doubled);
```

Write your result to `doubled`. You may assume it is large enough to hold the result. Return `doubled` when you are done.
~~~

"""

def double_char(s):
    return ''.join(c * 2 for c in s)
