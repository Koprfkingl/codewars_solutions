"""Kata - Is it a palindrome?

completed at: 2019-09-13 13:46:29
by: 

Write a function that checks if a given string (case insensitive) is a [palindrome](https://en.wikipedia.org/wiki/Palindrome). 

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as `madam` or `racecar`.
"""

def is_palindrome(s):
    if list(s.upper()) == list(reversed(s.upper())):
        return True
    else:
        return False
