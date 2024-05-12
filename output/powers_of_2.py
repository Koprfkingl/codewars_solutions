"""Kata - Powers of 2

completed at: 2022-02-28 18:09:02
by: Jakub Červinka

Complete the function that takes a non-negative integer `n` as input, and returns a list of all the powers of `2` with the exponent ranging from `0` to `n` ( inclusive ).

## Examples

```python
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
```
```bf
  n = String.fromCharCode(0)  ==> String.fromCharCode(1)
  n = String.fromCharCode(1)  ==> String.fromCharCode(1) + String.fromCharCode(2)
  n = String.fromCharCode(2)  ==> String.fromCharCode(1) + String.fromCharCode(2) + String.fromCharCode(4)
```
~~~if:lambdacalc
## Encodings

`purity: LetRec`  
`numEncoding: BinaryScott`  
export `foldr` for your `List` encoding
~~~

~~~if:riscv
RISC-V: The function signature is:

```c
void powers_of_two(size_t n, uint64_t powers[n + 1]);
```

Write the result to `powers`. You may assume it is large enough to hold the result. You should not return anything.
~~~
~~~if:bf
- Since BF doesn't have arrays, you should output each element individually.
- Outputs will always fit within a byte
~~~

"""

def powers_of_two(n):
    return [2**i for i in range(n+1)]
