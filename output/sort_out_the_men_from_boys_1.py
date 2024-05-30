"""Kata - Sort Out The Men  From Boys 

completed at: 2019-08-29 06:55:40
by: 

# Scenario 

*Now that the competition gets tough it will* **_Sort out the men from the boys_** . 

**_Men_** are the **_Even numbers_** and **_Boys_** are the **_odd_**   ![!alt](https://i.imgur.com/mdX8dJP.png) ![!alt](https://i.imgur.com/mdX8dJP.png) 

___
# Task

**_Given_** an *array/list [] of n integers* , **_Separate_** *The even numbers from the odds* , or **_Separate_**  **_the men from the boys_**  ![!alt](https://i.imgur.com/mdX8dJP.png) ![!alt](https://i.imgur.com/mdX8dJP.png)  
___
# Notes

* **_Return_** *an array/list where* **_Even numbers_** **_come first then odds_** 

* Since , **_Men are stronger than Boys_** , *Then* **_Even numbers_** in **_ascending order_** While **_odds in descending_** .

* **_Array/list_** size is *at least **_4_*** .

* **_Array/list_** numbers could be a *mixture of positives , negatives* .

* **_Have no fear_** , *It is guaranteed that no Zeroes will exists* . ![!alt](https://i.imgur.com/mdX8dJP.png)  

* **_Repetition_** of numbers in *the array/list could occur* , So **_(duplications are not included when separating)_**.
____
# Input >> Output Examples:

```
menFromBoys ({7, 3 , 14 , 17}) ==> return ({14, 17, 7, 3}) 
```

## **_Explanation_**:

**_Since_** , `{ 14 }` is the **_even number_** here , So it **_came first_** , **_then_** *the odds in descending order* `{17 , 7 , 3}`  .
____

```
menFromBoys ({-94, -99 , -100 , -99 , -96 , -99 }) ==> return ({-100 , -96 , -94 , -99})
```

## **_Explanation_**:

* **_Since_** , `{ -100, -96 , -94 }` is the **_even numbers_** here , So it **_came first_** in *ascending order *, **_then_** *the odds in descending order* `{ -99 }`

* **_Since_** , **_(Duplications are not included when separating)_** , *then* you can see **_only one (-99)_** *was appeared in the final array/list* . 
____

```
menFromBoys ({49 , 818 , -282 , 900 , 928 , 281 , -282 , -1 }) ==> return ({-282 , 818 , 900 , 928 , 281 , 49 , -1})
```

## **_Explanation_**:

* **_Since_** , `{-282 , 818 , 900 , 928 }` is the **_even numbers_** here , So it **_came first_** in *ascending order* , **_then_** *the odds in descending order* `{ 281 , 49 , -1 }`

* **_Since_** , **_(Duplications are not included when separating)_** , *then* you can see **_only one (-282)_** *was appeared in the final array/list* . 
____
____
___

# [Playing with Numbers Series](https://www.codewars.com/collections/playing-with-numbers)

# [Playing With Lists/Arrays Series](https://www.codewars.com/collections/playing-with-lists-slash-arrays)

# [Bizarre Sorting-katas](https://www.codewars.com/collections/bizarre-sorting-katas)

# [For More Enjoyable Katas](http://www.codewars.com/users/MrZizoScream/authored)
___

## ALL translations are welcomed

## Enjoy Learning !!
# Zizou

"""

def men_from_boys(arr):
    # your code here
    odd = []
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
            # to make list distinct (= remove duplicates), transfer it to set
            set_even = set(even)
            # set does not support + -> transfer back to list
            even = list(set_even)
            # print('even', even, 'set_even', set_even)
        else:
            odd.append(i)
            set_odd = set(odd)
            odd = list(set_odd)
            # print('odd', odd, 'set_odd', set_odd)
    odd.sort(reverse=True)
    even.sort()
    output = even + odd

    # print('odd:', odd, 'even', even)

    return output
