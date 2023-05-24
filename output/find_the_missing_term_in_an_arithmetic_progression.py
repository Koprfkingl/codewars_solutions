"""Kata - Find the missing term in an Arithmetic Progression

completed at: 2019-04-11 20:12:53
by: Jakub Červinka

An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP.  Find the missing term.  

You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.

## Example
```php
findMissing([1, 3, 5, 9, 11]) == 7
```
```csharp
Kata.FindMissing(new List<int> {1, 3, 5, 9, 11}) => 7
```
```fsharp
findMissing [| 1; 3; 5; 9; 11 |] = 7
```
```python
find_missing([1, 3, 5, 9, 11]) == 7
```
```swift
find_missing([1, 3, 5, 9, 11]) == 7
```
```ruby
findMissing([1, 3, 5, 9, 11]) == 7
```
```c
find_missing((const int[]){1,3,5,9,11}, 5)  => 7
```
```nasm
nums:  dw  1,3,5,9,11

mov rdi, nums
mov rsi, 5
call find_missing    ; EAX <- 7
```
```factor
{ 1 3 5 9 11 } find-missing ! => 7
```

PS: This is a sample question of the facebook engineer challenge on interviewstreet.
I found it quite fun to solve on paper using math, derive the algo that way.
Have fun!

"""

def find_missing(seq):
    diffs = [seq[i+1]-seq[i] for i in {0,1,2}]
    gain = max(set(diffs), key=diffs.count)
    for i, v in enumerate(seq):
        if seq[i+1] - v != gain:
            return v + gain

