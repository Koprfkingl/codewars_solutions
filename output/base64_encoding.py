"""Kata - Base64 Encoding

completed at: 2022-10-08 21:05:41
by: Jakub Červinka

Extend the String object (JS) or create a function (Python, C#) that converts the value of the String **to and from Base64** using the ASCII (UTF-8 for C#) character set.

### Example (input -> output):
```
'this is a string!!' -> 'dGhpcyBpcyBhIHN0cmluZyEh'
```

You can learn more about Base64 encoding and decoding <a href="http://en.wikipedia.org/wiki/Base64">here</a>.

Note: This kata uses the non-padding version ("=" is not added to the end).

"""

import base64

def to_base_64(string):
    return base64.b64encode(bytearray(string, 'utf-8')).decode("utf-8").replace('=', '')
    
def from_base_64(string):
    return base64.b64decode(bytearray(string, 'utf-8') + b'==').decode("utf-8") 
