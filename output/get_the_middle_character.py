"""Kata - Get the Middle Character

completed at: 2019-08-22 07:59:02
by: 

You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

```
Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"

```




#Input


A word (string) of length `0 < str < 1000` (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.



#Output


The middle character(s) of the word represented as a string.

"""

def get_middle(s):
    # your code here
    delka = len(s)
    odd = int((delka / 2)+0.5)
    even1 = int((delka / 2)-0.5)
    even2 = int((delka / 2)+0.5)
    zbytek = delka%2
    lichy_znak = s[odd]
    sudy_znak1 = s[even1]
    sudy_znak2 = s[even2]
    sudy_vystup = sudy_znak1 + sudy_znak2
    if zbytek == 0:
        print('delka zadaneho retezce je', delka)
        return sudy_vystup
    else:
        print('delka zadaneho retezce je', delka)
        return lichy_znak
