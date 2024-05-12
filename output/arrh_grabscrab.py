"""Kata - Arrh, grabscrab!

completed at: 2023-05-10 19:20:29
by: Jakub Červinka

Pirates have notorious difficulty with enunciating. They tend to blur all the letters together and scream at people.

At long last, we need a way to unscramble what these pirates are saying.

Write a function that will accept a jumble of letters as well as a dictionary, and output a list of words that the pirate might have meant.

For example:
```
grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
```

Should return `["sport", "ports"]`.

Return matches in the same order as in the dictionary. Return an empty array if there are no matches.

Good luck!


"""

from itertools import permutations
from functools import partial

def grabscrab(said, possible_words):
    
    def meets_condition(said, word):
        if len(word) != len(said): return False
        if set(word) != set(said): return False
        return sorted(word) == sorted(said)
    
    condition = partial(meets_condition, said)
    
    return list(filter(condition, possible_words))
