"""Kata - Is the date today

completed at: 2022-03-07 16:32:52
by: Jakub Červinka

Write a simple function that takes a `Date` as a parameter and returns a `Boolean` representing whether the date is today or not.

Make sure that your function does not return a false positive by only checking the day.
"""

from datetime import datetime

def is_today(date): 
    return datetime.today().date() == date.date()
