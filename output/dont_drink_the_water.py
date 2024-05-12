"""Kata - Don't Drink the Water

completed at: 2023-05-30 13:11:50
by: Jakub Červinka

Don't Drink the Water

Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear in the glass based on their density. (Lower density floats to the top) The width of the glass will not change from top to bottom.

```
======================
|   Density Chart    |
======================
| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |
----------------------

{                             {
  { 'H', 'H', 'W', 'O' },        { 'O','O','O','O' },
  { 'W', 'W', 'O', 'W' },  =>    { 'W','W','W','W' },
  { 'H', 'H', 'O', 'O' }         { 'H','H','H','H' }
}                             }
 
 ```
 
 The glass representation may be larger or smaller. If a liquid doesn't fill a row, it floats to the top and to the left.

"""

from itertools import chain

def separate_liquids(glass):
    if not glass:
        return []
    order = 'OAWH'
    elements = sorted(chain.from_iterable(glass), key=lambda x: order.index(x))
    args = [iter(elements)] * len(glass[0])  
    return list(map(list, zip(*args)))
        
