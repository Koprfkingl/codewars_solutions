"""Kata - Format words into a sentence

completed at: 2023-05-10 19:06:38
by: Jakub Červinka

Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string. 

Note:
* **Empty string** values should be ignored.
* **Empty arrays** or **null/nil/None** values being passed into the method should result in an empty string being returned. 

Example: **(Input --> output)**
```
['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
['ninja', '', 'ronin'] --> "ninja and ronin"
[] -->""
```
"""

def format_words(words):
    
    if not words: return ''
    
    words = [w for w in words if w]
    
    len_options = {
        0: lambda w: '',
        1: lambda w: w[0],
        2: lambda w: f'{w[0]} and {w[1]}'
    }
        
    return len_options.get(len(words), lambda w: f'{", ".join(w[:-1])} and {w[-1]}')(words)
        
