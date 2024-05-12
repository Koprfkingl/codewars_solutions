"""Kata - Count of positives / sum of negatives

completed at: 2022-05-14 14:44:24
by: Jakub Červinka

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

# Example

For input `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]`, you should return `[10, -65]`.
"""

def count_positives_sum_negatives(arr):
    
    if arr == []:
        return []
    
    pocet_pos = sum(1 for num in arr if num > 0)
    sum_neg = sum(num for num in arr if num < 0)
    return [pocet_pos, sum_neg]
