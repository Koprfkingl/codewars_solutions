"""Kata - Multiples of 3 or 5

completed at: 2019-02-17 20:20:46
by: Jakub Červinka

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 **below** the number passed in. 

~~~if:c,cobol,commonlisp,cpp,csharp,dart,elixir,factor,fsharp,javascript,julia,kotlin,lua,nasm,php,prolog,python,raqcket,ruby,rust,shell,swift,typescript,vb
Additionally, if the number is negative, return 0.
~~~

**Note:** If the number is a multiple of **both** 3 and 5, only count it *once*.
  
***Courtesy of projecteuler.net** ([Problem 1](https://projecteuler.net/problem=1))*

"""

def solution(number):
    i = 1
    res = 0
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            res += i
        i += 1
    return res
  
