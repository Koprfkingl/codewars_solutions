"""Kata - Simple Fun #79: Delete a Digit

completed at: 2023-06-01 20:46:10
by: Jakub Červinka

# Task
 Given an integer `n`, find the maximal number you can obtain by deleting exactly one digit of the given number.

# Example

 For `n = 152`, the output should be `52`;
 
 For `n = 1001`, the output should be `101`.
 
# Input/Output


 - `[input]` integer `n`

    Constraints: `10 ≤ n ≤ 1000000.`


 - `[output]` an integer
"""

def delete_digit(n):
    max_n = 0
    s = str(n)
    for i in range(len(s)):
        max_n = max(max_n, int(s[:i] + s[i + 1:]))
    return max_n
