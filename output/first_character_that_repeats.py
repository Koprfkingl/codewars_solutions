"""Kata - first character that repeats

completed at: 2023-09-04 19:32:40
by: Jakub Červinka

Find the first character that repeats in a String and return that character. 

```javascript
firstDup('tweet') => 't'
firstDup('like') => undefined
```
```python
first_dup('tweet') => 't'
first_dup('like') => None
```
```haskell
firstDup "tweet"         `shouldBe` Just 't'
firstDup (repeat ())     `shouldBe` Just ()
firstDup []              `shouldBe` Nothing
firstDup [1..10]         `shouldBe` Nothing
firstDup [2,46,3,1,1,2]  `shouldBe` 2
```
```ruby
first_dup('tweet') => 't'
first_dup('like') => nil
```

*This is not the same as finding the character that repeats first.*
*In that case, an input of 'tweet' would yield 'e'.*

Another example:

In `'translator'` you should return `'t'`, not `'a'`.
```
v      v  
translator
  ^   ^
```
While second `'a'` appears before second `'t'`, the first `'t'` is before the first `'a'`.
"""

def first_dup(s):
    for i, c in enumerate(s):
        if c in s[i + 1:]:
            return c
