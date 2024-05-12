"""Kata - Permute a Palindrome

completed at: 2023-09-04 19:30:27
by: Jakub Červinka

Write a function that will check whether ANY permutation of the characters  of the input string is a palindrome. Bonus points for a solution that is efficient and/or that uses _only_ built-in language functions. Deem yourself **brilliant** if you can come up with a version that does not use _any_ function whatsoever.

For this kata assume that all characters are **lowercase**.

# Example 

  `madam` -> True   
  `adamm` -> True   
  `junk`  -> False  
  
## Hint 
The brute force approach would be to generate _all_ the permutations of the string and check each one of them whether it is a palindrome. However, an optimized approach will not require this at all.  
"""

from collections import Counter

def permute_a_palindrome(_input): 
    c = Counter(_input)
    
    # one type of letter
    if len(c) == 1:
        return True
    
    # no two odds
    if sum(map(lambda n: n % 2, c.values())) > 1:
        return False
    
    return True
            
    
