"""Kata - Format a string of names like 'Bart, Lisa & Maggie'.

completed at: 2019-03-07 13:42:08
by: Jakub Červinka

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

``` ruby
list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

list([ {name: 'Bart'}, {name: 'Lisa'} ])
# returns 'Bart & Lisa'

list([ {name: 'Bart'} ])
# returns 'Bart'

list([])
# returns ''
```
``` elixir
list([ %{name: "Bart"}, %{name: "Lisa"}, %{name: "Maggie"} ])
# returns 'Bart, Lisa & Maggie'

list([ %{name: "Bart"}, %{name: "Lisa"} ])
# returns 'Bart & Lisa'

list([ %{name: "Bart"} ])
# returns 'Bart'

list([])
# returns ''
```
``` javascript
list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

list([ {name: 'Bart'}, {name: 'Lisa'} ])
// returns 'Bart & Lisa'

list([ {name: 'Bart'} ])
// returns 'Bart'

list([])
// returns ''
```
```python
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
```

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

"""

def namelist(names):
    family = [i['name'] for i in names]
    if len(names) > 1:
        return (f'{", ".join(family[:-1])} & {family[-1]}')
    else:
        return family[-1] if names else ''
