"""Kata - Find the Speedcuber's times!

completed at: 2019-10-31 11:10:25
by: 

Speedcubing is the hobby involving solving a variety of twisty puzzles, the most famous being the 3x3x3 puzzle or Rubik's Cube, as quickly as possible.

In the majority of Speedcubing competitions, a Cuber solves a scrambled cube 5 times, and their result is found by taking the average of the middle 3 solves (ie. the slowest and fastest times are disregarded, and an average is taken of the remaining times).

In some competitions, the unlikely event of a tie situation is resolved by comparing Cuber's fastest times.

Write a function ```cube_times(times)``` that, given an array of floats ```times``` returns an array / tuple with the Cuber's result (to 2 decimal places) AND their fastest solve.


For example:
```python
cube_times([9.5, 7.6, 11.4, 10.5, 8.1]) = (9.37, 7.6)
# Because (9.5 + 10.5 + 8.1) / 3 = 9.37 and 7.6 was the fastest solve.
```

```ruby
cube_times([9.5, 7.6, 11.4, 10.5, 8.1]) = [9.37, 7.6]
# Because (9.5 + 10.5 + 8.1) / 3 = 9.37 and 7.6 was the fastest solve.
```

```javascript
cubeTimes([9.5, 7.6, 11.4, 10.5, 8.1]) = [9.37, 7.6]
// Because (9.5 + 10.5 + 8.1) / 3 = 9.37 and 7.6 was the fastest solve.
```

```typescript
cubeTimes([9.5, 7.6, 11.4, 10.5, 8.1]) = [9.37, 7.6]
// Because (9.5 + 10.5 + 8.1) / 3 = 9.37 and 7.6 was the fastest solve.
```

```julia
cubetimes([9.5, 7.6, 11.4, 10.5, 8.1]) = (9.37, 7.6)
# Because (9.5 + 10.5 + 8.1) / 3 = 9.37 and 7.6 was the fastest solve.
```

Note: ```times``` will always be a valid array of 5 positive floats (representing seconds)
"""

def cube_times(times):

    averageLst = []
    minimum = min(times)
    maximum = max(times)
    for item in times:
        if item == minimum:
            pass
        elif item == maximum:
            pass
        else:
            averageLst.append(item)
    average = round(sum(averageLst) / len(averageLst), 2)
    output = [average, minimum]

    return tuple(output)
