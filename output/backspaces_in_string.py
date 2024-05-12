"""Kata - Backspaces in string

completed at: 2022-04-17 15:35:47
by: Jakub Červinka

Assume `"#"` is like a backspace in string. This means that string `"a#bc#d"` actually is `"bd"`

Your task is to process a string with `"#"` symbols.


## Examples

```
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
```
"""

def clean_string(s):
    s_l = []
    for c in s:
        if c != '#':
            s_l.append(c)
        else:
            try:
                s_l.pop()
            except IndexError:
                pass
    return ''.join(s_l)
