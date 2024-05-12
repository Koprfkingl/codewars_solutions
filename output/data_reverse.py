"""Kata - Data Reverse

completed at: 2022-03-27 21:18:53
by: Jakub Červinka

A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

```
11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
```

should become:

```
10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
```

The total number of bits will always be a multiple of 8.

The data is given in an array as such:

```
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
```

Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.
"""

from itertools import zip_longest, chain

def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or locks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def data_reverse(data):
    l = reversed(list(g for g in grouper(data, 8)))
    return list(chain.from_iterable(l))
    
    

