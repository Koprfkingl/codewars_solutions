"""Kata - Throwing Darts

completed at: 2023-05-22 20:11:18
by: Jakub Červinka

You've just recently been hired to calculate scores for a  Dart Board game!

Scoring specifications:

* 0 points - radius above 10
* 5 points - radius between 5 and 10 inclusive
* 10 points - radius less than 5

**If all radii are less than 5, award 100 BONUS POINTS!**

Write a function that accepts an array of radii (can be integers and/or floats), and returns a total score using the above specification.

An empty array should return 0.

## Examples:
```javascript
scoreThrows( [1, 5, 11] )    =>  15
scoreThrows( [15, 20, 30] )  =>  0
scoreThrows( [1, 2, 3, 4] )  =>  140
```
"""

def score_throws(radii):
    
    if not radii:
        return 0
    
    def score(r):
        if r > 10:
            return 0
        if r >= 5:
            return 5
        return 10
    
    bonus_points = 100 * all(r < 5 for r in radii)
    return sum(map(score, radii)) + bonus_points
