"""Kata - Data compression using run-length encoding

completed at: 2023-01-01 20:29:10
by: Jakub Červinka

[Run-length encoding](http://en.wikipedia.org/wiki/Run-length_encoding) (RLE) is a very simple form of lossless data compression in which runs of data are stored as a single data value and count.

A simple form of RLE would encode the string `"AAABBBCCCD"` as `"3A3B3C1D"` meaning, first there are `3 A`, then `3 B`, then `3 C` and last there is `1 D`.

Your task is to write a RLE encoder and decoder using this technique. The texts to encode will always consist of only uppercase characters, no numbers.
"""

import itertools
import re

def encode(s):
    return ''.join(f'{sum(1 for _ in g)}{k}' for k, g in itertools.groupby(s))
    
def decode(s):
    matches = re.finditer(r'(\d+)(.)', s)
    return ''.join(int(m[1]) * m[2] for m in matches)
