"""Kata - Mix Fruit Juice 

completed at: 2023-11-27 13:07:23
by: Jakub Červinka

## Story

Jumbo Juice makes a fresh juice out of fruits of your choice.Jumbo Juice charges $5 for regular fruits and $7 for special ones. Regular fruits are Banana, Orange, Apple, Lemon and Grapes. Special ones are Avocado, Strawberry and Mango. Others fruits that are not listed are also available upon request. Those extra special fruits cost $9 per each. There is no limit on how many fruits she/he picks.The price of a cup of juice is the mean of price of chosen fruits. In case of decimal number (ex. $5.99), output should be the nearest integer (use the standard rounding function of your language of choice). 

## Input

The function will receive an array of strings, each with the name of a fruit. The recognition of names should be case insensitive. There is no case of an empty array input.  


## Example

```
['Mango', 'Banana', 'Avocado'] //the price of this juice bottle is (7+5+7)/3 = $6($6.333333...)
```
"""

def mix_fruit(arr):
    regular_fruits = ['Banana', 'Orange', 'Apple', 'Lemon', 'Grapes']
    regular_price = 5
    reg_d = dict.fromkeys(regular_fruits, regular_price)
    
    special_fruits = ['Avocado', 'Strawberry', 'Mango']
    special_price = 7
    spec_d = dict.fromkeys(special_fruits, special_price)
    
    other_price = 9
    combined_dict = {k.lower(): v for k, v in (reg_d | spec_d).items()}
    
    total = sum(
        combined_dict.get(ingredient.lower(), other_price)
        for ingredient in arr
    )
    result = round(total / len(arr))
    
    return result
    
