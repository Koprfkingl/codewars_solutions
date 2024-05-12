"""Kata - Autocomplete! Yay!

completed at: 2023-05-24 17:59:41
by: Jakub Červinka

It's time to create an autocomplete function! Yay!

The autocomplete function will take in an input string and a dictionary array and return the values from the dictionary that start with the input string.  If there are more than 5 matches, restrict your output to the first 5 results.  If there are no matches, return an empty array.

Example:

```javascript
autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
```
```python
autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
```


For this kata, the dictionary will always be a valid array of strings.
Please return all results in the order given in the dictionary, even if they're not always alphabetical.
The search should NOT be case sensitive, but the case of the word should be preserved when it's returned.

For example, "Apple" and "airport" would both return for an input of 'a'.  However, they should return as "Apple" and "airport" in their original cases.

<div style="background:#ffa; color:#000; padding:10px;">
<p>Important note:
<p>Any input that is NOT a letter should be treated as if it is not there.  For example, an input of "$%^" should be treated as "" and an input of "ab*&1cd" should be treated as "abcd".
<p>(Thanks to wthit56 for the suggestion!)
</div>

"""

def autocomplete(input_, dictionary):
    inp = ''.join(filter(str.isalpha, input_))
    return [w for w in dictionary if w.lower().startswith(inp.lower())][:5]
