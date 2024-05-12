"""Kata - Stop gninnipS My sdroW!

completed at: 2019-03-05 11:35:58
by: Jakub Červinka

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:
```
"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
```
"""

def spin_words(sentence):
    
    return ' '.join(w[::-1] if len(w) >= 5 else w for w in sentence.split()) 
