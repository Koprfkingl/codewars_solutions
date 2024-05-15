"""Kata - Find the Strongest Apes

completed at: 2024-05-14 18:45:48
by: Jakub Červinka

Imagine that you went to a zoo and some zoologists asked you for help.
They want you to find the strongest ape of its own kind and there are 4 types of apes in the zoo. (Gorilla, Gibbon, Orangutan, Chimpanzee)

* There will be only one parameter which is a list containing lots of dictionaries.
* Each dictionary will be like this: `{"name": name, "weight": weight, "height": height, "type": type}`
* To find the strongest ape, you need to compare the sum of weight and height of each apes of that kind.
* The ape with the highest weight and height will be the strongest ape.
* You need to return a dictionary which contains the names of the strongest apes of all kinds.`{"Gorilla": strongest_gorilla, "Gibbon": strongest_gibbon, "Orangutan": strongest_orangutan, "Chimpanzee": strongest_chimpanzee}`
* There can be 2 or more apes which has the same highest weight and height. In that case, you need to sort their names by alphabet and then choose the first one as the strongest ape.
* If there are no apes for a kind (e.g. Gorilla), you need to return a dictionary like this: `{"Gorilla": None, "Gibbon": strongest_gibbon, "Orangutan": strongest_orangutan, "Chimpanzee": strongest_chimpanzee}`

__Example 1:__
```
find_the_strongest_apes(
            [{"name": "aba", "weight": 101, "height": 99, "type": "Gorilla"},
             {"name": "abb", "weight": 99, "height": 101, "type": "Gorilla"},
             {"name": "abc", "weight": 101, "height": 99, "type": "Orangutan"},
             {"name": "abd", "weight": 99, "height": 101, "type": "Orangutan"}])
```
Should return `{'Gorilla': 'aba', 'Gibbon': None, 'Orangutan': 'abc', 'Chimpanzee': None}`

__Example 2:__
```
find_the_strongest_apes(
            [{"name": "aba", "weight": 140, "height": 120, "type": "Gorilla"},
             {"name": "abb", "weight": 20, "height": 50, "type": "Gibbon"},
             {"name": "abc", "weight": 75, "height": 110, "type": "Orangutan"},
             {"name": "abd", "weight": 50, "height": 100, "type": "Chimpanzee"}])
```
Should return `{'Gorilla': 'aba', 'Gibbon': 'abb', 'Orangutan': 'abc', 'Chimpanzee': 'abd'}`

__Example 3:__
```
find_the_strongest_apes(
            [{"name": "aba", "weight": 140, "height": 120, "type": "Gorilla"},
             {"name": "abb", "weight": 150, "height": 120, "type": "Gorilla"},
             {"name": "abc", "weight": 75, "height": 110, "type": "Orangutan"},
             {"name": "abd", "weight": 50, "height": 100, "type": "Chimpanzee"}])
```
Should return `{'Gorilla': 'abb', 'Gibbon': None, 'Orangutan': 'abc', 'Chimpanzee': 'abd'}`

_*English is not my native language, so some sentences may not be descriptive enough or even give incorrect information. If you find a wrong sentence, please feel free to comment._
"""

from dataclasses import dataclass
from dataclasses import field
from collections import defaultdict
from itertools import groupby
from operator import attrgetter


@dataclass
class Ape:
    type: str
    power: int = field(init=False)
    weight: int
    height: int
    name: str
    
    def __post_init__(self):
        self.power = self.weight + self.height
    
    def __str__(self):
        return f'{self.type} {self.name!r} p: {self.power}'
    
    __repr__ = __str__


sort_fn = lambda x: (x.type, -x.power, x.name)
    
    
def find_the_strongest_apes(_list):
    types = ('Gorilla', 'Gibbon', 'Orangutan', 'Chimpanzee')
    result = dict.fromkeys(types, None)
    
    monkes = sorted((Ape(**data) for data in _list), key=sort_fn)
    
    for _, apes in groupby(monkes, key=attrgetter('type')):
        ape = next(apes)
        result[ape.type] = ape.name

    return result
        
    
    
