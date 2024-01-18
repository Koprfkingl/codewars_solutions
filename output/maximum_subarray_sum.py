"""Kata - Maximum  subarray sum

completed at: 2023-06-14 12:30:04
by: Jakub Červinka

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

```haskell
maxSequence [-2, 1, -3, 4, -1, 2, 1, -5, 4]
-- should be 6: [4, -1, 2, 1]
```
```javascript
maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
// should be 6: [4, -1, 2, 1]
```
```python
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
```
```clojure
(max-sequence [-2, 1, -3, 4, -1, 2, 1, -5, 4])
;; should be 6: [4, -1, 2, 1]
```
```java
Max.sequence(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4});
// should be 6: {4, -1, 2, 1}
```
```scala
Max.sequence(Array(-2, 1, -3, 4, -1, 2, 1, -5, 4));
// should be 6: Array(4, -1, 2, 1)
```
```kotlin
maxSequence(listOf(-2, 1, -3, 4, -1, 2, 1, -5, 4));
// should be 6: listOf(4, -1, 2, 1)
```
```c
maxSequence({-2, 1, -3, 4, -1, 2, 1, -5, 4}, 9)
// should return 6, from sub-array: {4, -1, 2, 1}
```
```cpp
maxSequence({-2, 1, -3, 4, -1, 2, 1, -5, 4});
//should be 6: {4, -1, 2, 1}
```
```rust
max_sequence(&[-2, 1, -3, 4, -1, 2, 1, -5, 4]);
//should be 6: [4, -1, 2, 1]
```
```cobol
       maxSequence [-2, 1, -3, 4, -1, 2, 1, -5, 4]
      * should be 6: [4, -1, 2, 1]
```

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

"""

def max_sequence(arr):
    if not arr:
        return 0
    if all(n < 0 for n in arr):
        return 0
    current_sum =best_sum = 0
    for x in arr:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
