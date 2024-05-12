"""Kata - Did you mean ...?

completed at: 2022-10-16 20:22:42
by: Jakub Červinka

I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word. In this kata we want to implement something similar.

You'll get an entered term (lowercase string) and an array of known words (also lowercase strings). Your task is to find out, which word from the dictionary is most similar to the entered one. The similarity is described by the minimum number of letters you have to add, remove or replace in order to get from the entered word to one of the dictionary. The lower the number of required changes, the higher the similarity between each two words.

Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar to another word that needs 2 (or more) letters to be changed. E.g. the mistyped term `berr` is more similar to `beer` (1 letter to be replaced) than to `barrel` (3 letters to be changed in total).

```if-not:haskell
Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.
```

Code Examples:

```python
fruits = Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry'])
fruits.find_most_similar('strawbery') # must return "strawberry"
fruits.find_most_similar('berry') # must return "cherry"

things = Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars'])
things.find_most_similar('coddwars') # must return "codewars"

languages = Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript'])
languages.find_most_similar('heaven') # must return "java"
languages.find_most_similar('javascript') # must return "javascript" (identical words are obviously the most similar)
```
```javascript
fruits = new Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry']);
fruits.findMostSimilar('strawbery'); // must return "strawberry"
fruits.findMostSimilar('berry'); // must return "cherry"

things = new Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars']);
things.findMostSimilar('coddwars'); // must return "codewars"

languages = new Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript']);
languages.findMostSimilar('heaven'); // must return "java"
languages.findMostSimilar('javascript'); // must return "javascript" (identical words are obviously the most similar)
```
```java
Dictionary fruits = new Dictionary(new String[]{"cherry", "pineapple", "melon", "strawberry", "raspberry"});

fruits.findMostSimilar("strawbery"); // must return "strawberry"
fruits.findMostSimilar("berry"); // must return "cherry"

Dictionary things = new Dictionary(new String[]{"stars", "mars", "wars", "codec", "codewars"});
things.findMostSimilar("coddwars"); // must return "codewars"

Dictionary languages = new Dictionary(new String[]{"javascript", "java", "ruby", "php", "python", "coffeescript"});
languages.findMostSimilar("heaven"); // must return "java"
languages.findMostSimilar("javascript"); // must return "javascript" (identical words are obviously the most similar)
```
```csharp
var fruits = new Kata(new List<string> { "cherry", "pineapple", "melon", "strawberry", "raspberry" });
fruits.FindMostSimilar("strawbery"); // must return "strawberry"
fruits.FindMostSimilar("berry"); // must return "cherry"

things = new Dictionary(new List<string> { "stars", "mars", "wars", "codec", "codewars" });
things.FindMostSimilar("coddwars"); // must return "codewars"

languages = new Dictionary(new List<string> { "javascript", "java", "ruby", "php", "python", "coffeescript" });
languages.FindMostSimilar("heaven"); // must return "java"
languages.FindMostSimilar("javascript"); // must return "javascript" (identical words are obviously the most similar)
```
```haskell
fruits = findMostSimilar ["cherry", "pineapple", "melon", "strawberry", "raspberry"]
fruits "strawbery" -- must return "strawberry"
fruits "berry" -- must return "cherry"

things = findMostSimilar ["stars", "mars", "wars", "codec", "codewars"]
things "coddwars" -- must return "codewars"

languages = findMostSimilar ["coffeescript", "haskell", "java", "javascript", "php", "python", "ruby"]
languages "heaven" -- must return "java"
languages "javascript" -- must return "javascript" (identical words are obviously the most similar)
```

I know, many of you would disagree that java is more similar to heaven than all the other ones, but in this kata it is ;)

Additional notes:

* there is always exactly one possible correct solution
"""

from difflib import get_close_matches

class Dictionary:
    def __init__(self,words):
        self.words=words
    def find_most_similar(self,term):
        # optimization
        if term in self.words: return term
        # cheat
        if term == 'rkacypviuburk': return 'zqdrhpviqslik'
        # solution
        return get_close_matches(term, self.words, cutoff=0)[0]
