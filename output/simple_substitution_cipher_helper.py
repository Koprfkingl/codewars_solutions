"""Kata - Simple Substitution Cipher Helper

completed at: 2023-06-22 11:20:54
by: Jakub Červinka

A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

E.g.
```javascript
var abc1 = "abcdefghijklmnopqrstuvwxyz";
var abc2 = "etaoinshrdlucmfwypvbgkjqxz";
   
var sub = new SubstitutionCipher(abc1, abc2);
sub.encode("abc") // => "eta"
sub.encode("xyz") // => "qxz"
sub.encode("aeiou") // => "eirfg"
   
sub.decode("eta") // => "abc"
sub.decode("qxz") // => "xyz"
sub.decode("eirfg") // => "aeiou"
```
```python
map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";
   
cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"
   
cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"
```
```rust
let map1 = "abcdefghijklmnopqrstuvwxyz";
let map2 = "etaoinshrdlucmfwypvbgkjqxz";
   
let cipher = Cipher::new(map1, map2);
cipher.encode("abc") // => "eta"
cipher.encode("xyz") // => "qxz"
cipher.encode("aeiou") // => "eirfg"
   
cipher.decode("eta") // => "abc"
cipher.decode("qxz") // => "xyz"
cipher.decode("eirfg") // => "aeiou"
```

If a character provided is not in the opposing alphabet, simply leave it as be.
"""


class Cipher(object):
    def __init__(self, map1, map2):
        self.enc_m = str.maketrans(map1, map2)
        self.dec_m = str.maketrans(map2, map1)
    
    def encode(self, s):
        return s.translate(self.enc_m)
    
    def decode(self, s):
        return s.translate(self.dec_m)
