"""Kata - Simple multiplication

completed at: 2023-05-30 10:35:41
by: Jakub Červinka

This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""

def simple_multiplication(n) :
    return n * 8 if n % 2 == 0 else n * 9
