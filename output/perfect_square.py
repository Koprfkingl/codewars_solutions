"""Kata - Perfect Square.

completed at: 2023-09-29 17:17:24
by: Jakub Červinka

<style>

  .firstRow {
    vertical-align:-60px;
  }

</style>

<h4 style="color:brown">Task</h4>

Write function which validates an input string. If the string is a perfect square return true,false otherwise.

<h4 style="color:brown">What is perfect square?</h4>
* We assume that character '.' (dot) is a perfect square (1x1)
* Perfect squares can only contain '.' (dot) and optionally '\n' (line feed) characters.<br>
* Perfect squares must have same width and height -> cpt.Obvious<br>
* Squares of random sizes will be tested!

<h4 style="color:brown">Function input:</h4>

```javascript
perfectSquare = "...\n...\n...";    

// This represents the following Perfect Square:

`...
 ...
 ...`
                               
notPerfect = "..,\n..\n...";

// This is not a Perfect Square:

`..,
 ..
 ...`

```

"""

def perfect_square(square):
    rows = square.split('\n')
    return all(
        row == '.' * len(rows)
        for row in rows
    )
