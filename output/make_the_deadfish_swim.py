"""Kata - Make the Deadfish Swim

completed at: 2019-02-17 09:08:36
by: Jakub Červinka

Write a simple parser that will parse and run Deadfish.  

Deadfish has 4 commands, each 1 character long:
* `i` increments the value (initially `0`)
* `d` decrements the value
* `s` squares the value
* `o` outputs the value into the return array

Invalid characters should be ignored.

```javascript
parse("iiisdoso") => [ 8, 64 ]
```
```csharp
Deadfish.Parse("iiisdoso") => new int[] {8, 64};
```
```python
parse("iiisdoso")  ==>  [8, 64]
```
```haskell
parse "iiisdoso" -> [ 8, 64 ]
```
```c
parse("iiisdoso") == {8, 64}
```
```go
Parse("iiisdoso") == []int{8, 64}
```
```ruby
parse("iiisdoso")  ==>  [8, 64]
```
```java
Deadfish.parse("iiisdoso") =- new int[] {8, 64};
```
```groovy
DeadFish.parse("iiisdoso")  ==>  [8, 64]
```
```scala
Deadfish.parse("iiisdoso") => List(8, 64)
```
```typescript
parse("iiisdoso") => [8, 64]
```
```julia
deadfish("iiisdoso") --> [8, 64]
```
```powershell
Eval-DeadFish -Data "ooo" --> @(0, 0, 0)  # [long[]]

```
```factor
"iiisdoso" deadfish -> { 8 64 }
```

"""

def parse(data):
    val = 0
    res = []
    
    opers = {
        'i': lambda x: x+1,
        'd': lambda x: x-1,
        's': lambda x: x**2,
        }
        
    for s in data:
        if s == 'o':
            res.append(val)
        try:
            val = opers[s](val)
        except KeyError:
            pass
            
    return res        
        
