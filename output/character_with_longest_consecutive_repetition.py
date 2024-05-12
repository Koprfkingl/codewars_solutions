"""Kata - Character with longest consecutive repetition

completed at: 2022-12-05 22:01:09
by: Jakub Červinka

For a given string `s` find the character `c` (or `C`) with longest consecutive repetition and return:

```c
c
(assign l to pointer)
```
```cpp
std::pair<char, unsigned int>(c, l)
```
```lua
{ character = c, length = l }
```
```go
type Result struct {
	C rune // character
	L int  // count
}
```
```python
(c, l)
```
```haskell
Just (Char, Int)
```
```csharp
Tuple<char?, int>(c, l)
```
```shell
# in Shell a String of comma-separated values
c,l
```
```javascript
[c, l]
```
```php
[$c, $l]
```
```ruby
[c, l]
```
```groovy
[c, l]
```
```coffeescript
[c, l]
```
```java
Object[]{c, l};
```
```typescript
[c, l]: [string, number]
```
```scala
Some(c, l)
```
```ocaml
Some (c, l)
```
```nim
(c, l)
```
```kotlin
Pair(c, l)
```
```vb
Tuple(Of Char?, Integer>(c, l)
```
```elixir
{c, l}
```
```rust
Some((c, l))
```
```perl
[c, l]
```


where `l` (or `L`) is the length of the repetition. If there are two or more characters with the same `l` return the first in order of appearance.

For empty string return:

```c
'\0'
(assign 0 to pointer)
```
```cpp
std::nullopt
```
```lua
{character = "", length = 0 }
```
```go
Result{}
```
```python
('', 0)
```
```haskell
Nothing
```
```csharp
Tuple<char?, int>(null, 0)
```
```shell
,0
```
```javascript
["", 0]
```
```php
["", 0]
```
```groovy
["", 0]
```
```ruby
["", 0]
```
```coffeescript
["", 0]
```
```java
Object[]{"", 0}
```
```typescript
["", 0]
```
```scala
None
```
```ocaml
None
```
```nim
('\0', 0)
```
```kotlin
Pair(null, 0)
```
```vb
Tuple(Of Char?, Integer)(Nothing, 0)
```
```elixir
{"", 0}
```
```rust
None
```
```swift
["": 0]
```
```perl
["", 0]
```

Happy coding! :)

"""

def longest_repetition(chars):
    from itertools import groupby
    if not chars: return '', 0
    groups = [(k, list(g)) for k, g in groupby(chars[::-1])]
    groups.sort(key=lambda x: len(x[1]))
    c, l = groups[-1]
    return c, len(l)
