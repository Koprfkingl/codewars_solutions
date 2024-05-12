"""Kata - String average

completed at: 2023-06-28 12:32:10
by: Jakub Červinka

You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"






"""

from statistics import mean
from math import floor

ERROR_S = 'n/a'

def average_string(s):
    if not s:
        return ERROR_S
    
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    reversed_number_dict = {v: k for k, v in number_dict.items()}
    try:
        nums = [
            number_dict[text]
            for text in s.split()
        ]
    except KeyError:
        return ERROR_S
    rounded_mean = floor(mean(nums))
    return reversed_number_dict[rounded_mean]
        


