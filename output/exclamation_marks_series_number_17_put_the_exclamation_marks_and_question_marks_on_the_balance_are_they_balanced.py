"""Kata - Exclamation marks series #17: Put the exclamation marks and question marks on the balance - are they balanced?

completed at: 2023-02-05 19:36:33
by: Jakub Červinka

Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings `left` and `right` on the balance - are they balanced?
 
If the left side is more heavy, return `"Left"`; if the right side is more heavy, return `"Right"`; if they are balanced, return `"Balance"`.

## Examples

```python
"!!", "??"     -->  "Right"
"!??", "?!!"   -->  "Left"
"!?!!", "?!?"  -->  "Left"
"!!???!????", "??!!?!!!!!!!"  -->  "Balance"
```
```haskell
-- For Haskell use the Comparison type defined in Preloaded code
-- data Comparison = Left | Right | Balance deriving (Show, Eq, Enum, Bounded)

balance :: String -> String -> Comparison

balance "!!" "??" == Right
balance "!??" "?!!" == Left
balance "!?!!" "?!?" == Left
balance "!!???!????" "??!!?!!!!!!!" == Balance
```
"""

def balance(left, right):
    left_w = sum(2 if c == '!' else 3 for c in left)
    right_w = sum(2 if c == '!' else 3 for c in right)
    balance = left_w - right_w
    if balance == 0:
        return 'Balance'
    return 'Left' if balance > 0 else 'Right'
    
    
  
