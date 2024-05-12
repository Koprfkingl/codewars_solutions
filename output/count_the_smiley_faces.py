"""Kata - Count the smiley faces!

completed at: 2019-03-06 19:39:04
by: Jakub Červinka

Given an array (arr) as an argument complete the function `countSmileys` that should return the total number of smiling faces.  

Rules for a smiling face:
- Each smiley face must contain a valid pair of eyes. Eyes can be marked as `:` or `;`
- A smiley face can have a nose but it does not have to. Valid characters for a nose are `-` or `~`
- Every smiling face must have a smiling mouth that should be marked with either `)` or `D`

No additional characters are allowed except for those mentioned.  

**Valid smiley face examples:** `:) :D ;-D :~)`  
**Invalid smiley faces:**  `;( :> :} :]`

## Example

```
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
```

## Note

In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

"""

def count_smileys(arr):
    return sum(map(lambda i: i[0] in ':;' and i[1] not in '*o' and i[-1] in ')D', arr))
