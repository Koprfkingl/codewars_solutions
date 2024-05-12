"""Kata - The Vowel Code

completed at: 2022-04-17 18:24:58
by: Jakub Červinka

**Step 1:** Create a function called `encode()` to replace all the lowercase vowels in a given string with numbers according to the following pattern:
```
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
```

For example, `encode("hello")` would return `"h2ll4"`. There is no need to worry about uppercase vowels in this kata.

**Step 2:** Now create a function called `decode()` to turn the numbers back into vowels according to the same pattern shown above.

For example, `decode("h3 th2r2")` would return `"hi there"`.

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

"""

letters = 'aeiou'
numbers = '12345'

def encode(st):
    tb = str.maketrans(letters, numbers)
    return st.translate(tb)
    
def decode(st):
    tb = str.maketrans(numbers, letters)
    return st.translate(tb)
