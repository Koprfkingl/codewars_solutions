"""Kata - Convert string to camel case

completed at: 2022-03-25 12:42:25
by: Jakub Červinka

Complete the method/function so that it converts dash/underscore delimited words into [camel casing](https://en.wikipedia.org/wiki/Camel_case). The first word within the output should be capitalized **only** if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

### Examples

`"the-stealth-warrior"` gets converted to `"theStealthWarrior"` 
 
`"The_Stealth_Warrior"` gets converted to `"TheStealthWarrior"`

`"The_Stealth-Warrior"` gets converted to `"TheStealthWarrior"`

"""

import re
def to_camel_case(text):
    if not text:
        return ''
    text = re.sub(r'[-_]', ' ', text)
    capitals = ''.join(w.title() for w in text.split())
    if text[0].isupper():
        return capitals 
    else:
        return capitals[0].lower() + capitals[1:]
