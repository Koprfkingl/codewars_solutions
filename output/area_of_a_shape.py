"""Kata - Area of a Shape

completed at: 2024-05-14 16:44:00
by: Jakub Červinka

We'd like to know the area of an arbitrary shape. The only information of the shape is that it is bounded within the square area of four points: (0, 0), (1, 0), (1, 1) and (0, 1).

Given a function `f(x, y)` which returns a boolean representing whether the point `(x, y)` is inside the shape, determine the area of the shape. Your answer is allowed to differ from the true answer by at most 0.01.

Hint: http://bit.ly/1vJJt61
"""

from random import random as rand

def area_of_the_shape(f):
    n = 10_000
    inside = sum(f(rand(), rand()) for _ in range(n))
    return inside / n
