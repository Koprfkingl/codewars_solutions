"""Kata - Playing with passphrases

completed at: 2019-05-06 14:26:08
by: Jakub Červinka

Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently
they can be guessed due to common cultural references.
You  can get your passphrases stronger by different means. One is the following:

choose a text in capital letters including or not digits and non alphabetic characters,
 
1. shift each letter by a given number but the transformed letter must be a letter (circular shift), 
2. replace each digit by its complement to 9, 
3. keep such as non alphabetic and non digit characters, 
4. downcase each letter in odd position, upcase each letter in even position (the first character is in position 0), 
5. reverse the whole result.

#### Example:

your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"

With longer passphrases it's better to have a small and easy program.
Would you write it?

https://en.wikipedia.org/wiki/Passphrase
"""

from string import maketrans
from string import ascii_lowercase as asc_low
from string import digits

def play_pass(s, n):
    
    def shiftN(phrase, n):
         
        phrase = phrase.lower()
        rotated = asc_low[n:] + asc_low[:n]
        translation = maketrans(asc_low, rotated)
        return phrase.translate(translation)
        
    def change_nums(phrase):
        return ''.join([str(9 - int(ch)) if ch in digits else ch for ch in phrase])
          
    def recapitalize(phrase):
        return ''.join([ch.lower() if i % 2 == 1 else ch.upper() for i, ch in enumerate(phrase)])
        
    def reverse(phrase):
        return phrase[::-1]
    
    phrase = shiftN(s, n)
    phrase = change_nums(phrase)
    phrase = recapitalize(phrase)
    phrase = reverse(phrase)
    
    return phrase
        
        
