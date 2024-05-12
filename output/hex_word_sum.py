"""Kata - Hex Word Sum

completed at: 2019-02-09 20:44:29
by: Jakub Červinka

### Description
As hex values can include letters `A` through to `F`, certain English words can be spelled out, such as `CAFE`, `BEEF`, or `FACADE`.
This vocabulary can be extended by using numbers to represent other letters, such as `5EAF00D`, or `DEC0DE5`.

Given a string, your task is to return the decimal sum of all words in the string that can be interpreted as such hex values.


### Example

Working with the string `"BAG OF BEES"`:
```
"BAG"  =  0, as it is not a valid hex value  
"OF"   =  0F   =  15
"BEES" =  BEE5 =  48869
```
So the result is the sum of these: 48884 (0 + 15 + 48869)


### Notes
* Inputs are all uppercase and contain no punctuation
* `0` can be substituted for `O`
* `5` can be substituted for `S`

"""

import string

def hex_word_sum(sentence):
    sum = 0
    
    if len(sentence) == 0:
        return 0
    
    for word in sentence.split(' '):
        
        if all(c in string.hexdigits for c in word):
              sum += int(word, 16)
        else:
              new_w = word.replace('O', '0').replace('S', '5')
             
              if all(c in string.hexdigits for c in new_w):
                  sum += int(new_w, 16)
        
            
    return sum
