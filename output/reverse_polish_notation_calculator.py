"""Kata - Reverse polish notation calculator

completed at: 2019-04-25 07:34:21
by: Jakub Červinka

Your job is to create a calculator which evaluates expressions in [Reverse Polish notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

For example expression `5 1 2 + 4 * + 3 -` (which is equivalent to `5 + ((1 + 2) * 4) - 3` in normal notation) should evaluate to `14`.

For your convenience, the input is formatted such that a space is provided between every token.

Empty expression should evaluate to `0`.

Valid operations are `+`, `-`, `*`, `/`.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
"""

def calc(expr):
    expr = expr.split()
    stack = []
    
    operands = {'+', '-', '*', '/'}
    
    for elem in expr:
        if elem in operands and stack:
            stack.append(str(eval(stack.pop(-2) + elem + stack.pop())))
        else:
            stack.append(elem)
    
    return float(stack[0]) if stack else 0
