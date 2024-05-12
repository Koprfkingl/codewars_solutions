"""Kata - Is Integer Array?

completed at: 2023-05-04 12:05:35
by: Jakub Červinka

Write a function with the signature shown below:
```javascript
function isIntArray(arr) {
  return true
}
```
```python
def is_int_array(arr):
    return True
```
```ruby
def is_int_array(arr)
  true
end
```
* returns `true  / True`  if every element in an array is an integer or a float with no decimals.
* returns `true  / True`  if array is empty.
* returns `false / False` for every other input.


"""

def is_int_array(arr):
    if arr == '':
        return False
    try:
        return all(int(c) == c for c in arr)
    except:
        return False
