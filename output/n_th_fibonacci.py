"""Kata - N-th Fibonacci

completed at: 2022-04-17 18:31:03
by: Jakub Červinka

I love Fibonacci numbers in general, but I must admit I love some more than others. 

I would like for you to write me a function that, when given a number `n` (`n >= 1` ), returns the n<sup>th</sup> number in the Fibonacci Sequence.

For example:

```javascript
   nthFibo(4) == 2
```
```coffeescript
   nthFibo(4) == 2
```
```ruby
   nth_fibonacci(4) == 2
```
```haskell
   fib 4 == 2
```
```lambdacalc
   nth-fibo 4 == 2
```
```python
   nth_fib(4) == 2
```
```csharp
   NthFib(4) == 2
```
```c
   nth_fib(4) == 2
```
```julia
   nthfibo(4) == 2
```
```lua
   nth_fib(4) == 2
```
```nasm
    mov edi, 4
    call nth_fib
    cmp rax, 2 ; should be equal
```

Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are `0` and `1`, and each subsequent number is the sum of the previous two.

~~~if: lua
Note: Since the 94th term of the sequence would cause an overflow in Lua, n will be between 0 and 93 (inclusive).
~~~

~~~if:lambdacalc
#### Encodings

`numEncoding: BinaryScott`
~~~

"""

def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def nth_fib(n):
    fb = fib_gen()
    for _ in range(n - 1):
        next(fb)
    return next(fb)
