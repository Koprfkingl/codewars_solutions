"""Kata - Strip Comments

completed at: 2024-05-25 18:48:14
by: 

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out. 

**Example:**

Given an input string of:
```
apples, pears # and bananas
grapes
bananas !apples
```

The output expected would be:
```
apples, pears
grapes
bananas
```

The code would be called like so:

```javascript
var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
// result should == "apples, pears\ngrapes\nbananas"

```

```kotlin
var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", charArrayOf('#', '!'))
// result should == "apples, pears\ngrapes\nbananas"

```

```coffeescript
result = stripComments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\nograpes\nbananas"

```

```ruby
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

```

```crystal
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

```

```python
result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

```

```csharp
string stripped = StripCommentsSolution.StripComments("apples, pears # and bananas\ngrapes\nbananas !apples", new [] { "#", "!" })
// result should == "apples, pears\ngrapes\nbananas"
```

```julia
result = stripcomments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
```

```factor
"apples, pears # and bananas\ngrapes\nbananas !apples"
"#!"
strip-comments ! "apples, pears\ngrapes\nbananas"
```

```scala
val res = stripComments("apples, pears # and bananas\ngrapes\nbananas !apples", Set('#', '!'))
// res should be "apples, pears\ngrapes\nbananas"
```

"""

def strip_comments(strng, markers):
    # non regex solution on purpose
    
    # split string into list of lines
    listOfLines = strng.split('\n')

    output = []

    # for each line
    for line in listOfLines:
        
        # if line is not empty and markers list is not empty
        if line and markers:
            # find the first marker in the line
            first_marker_index = (
                min(
                    [line.find(marker) 
                     if marker in line 
                     else 
                        len(line) 
                     for marker in markers]))

            # check whitespace before marker
            if line[first_marker_index - 1] == ' ':
                output.append(line[:first_marker_index - 1].rstrip())
            else:
                output.append(line[:first_marker_index].rstrip())
        else:
            # if line is empty or markers list is empty, add the whole line
            output.append(line)

    output = '\n'.join(output)
    return output

