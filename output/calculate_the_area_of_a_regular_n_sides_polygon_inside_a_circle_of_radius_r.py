"""Kata - Calculate the area of a regular n sides polygon inside a circle of radius r

completed at: 2023-06-22 12:21:20
by: Jakub Červinka

Write the following function:

```javascript
function areaOfPolygonInsideCircle(circleRadius, numberOfSides)
```
```haskell
areaOfPolygonInsideCircle :: Double -> Int -> Double
areaOfPolygonInsideCircle circleRadius numberOfSides = undefined
```
```php
function areaOfPolygonInsideCircle($circleRadius, $numberOfSides)
```
```csharp
public static double AreaOfPolygonInsideCircle(double circleRadius, int numberOfSides)
```
```clojure
(defn area-of-polygon-inside-circle [circle-radius number-of-sides]
```
```python
def area_of_inscribed_polygon(circle_radius, number_of_sides):
```
```elixir
def area_of_polygon_inside_circle(circle_radius, number_of_sides) do
```
```ruby
def area_of_polygon_inside_circle(circle_radius, number_of_sides)
```
```crystal
def area_of_polygon_inside_circle(circle_radius, number_of_sides)
```
```groovy
static double areaOfPolygonInsideCircle(circleRadius, numberOfSides)
```
```cpp
double areaOfPolygonInsideCircle (double circleRadius , int numberOfSides)
```
```swift
areaOfPolygonInsideCircle(_ circleRadius: Double, _ numberOfSides: Int) -> Double
```
```objc
double area_of_polygon_inside_circle(double circle_radius, int number_of_sides);
```
```c
double area_of_polygon_inside_circle(double circle_radius, int number_of_sides);
```
```dart
double areaOfPolygonInsideCircle(double circleRadius, int numberOfSides)
```
```coffeescript
areaOfPolygonInsideCircle = (circleRadius, numberOfSides)
```
```typescript
export function areaOfPolygonInsideCircle(circleRadius: number, numberOfSides: number): number
```
```java
public static double areaOfPolygonInsideCircle(double circleRadius, int numberOfSides) 
```
```coffeescript
areaOfPolygonInsideCircle = (circleRadius, numberOfSides)
```
```go
func AreaOfPolygonInsideCircle(circleRadius float64, numberOfSides int) float64
```
```nasm
area_of_polygon_inside_circle(circle_radius, number_of_sides)
```
```rust
fn area_of_polygon_inside_circle(circle_radius: f64, number_of_sides: i32) -> f64
```

It should calculate the area of a regular polygon of `numberOfSides`, `number-of-sides`, or `number_of_sides` sides inside a circle of radius `circleRadius`, `circle-radius`, or `circle_radius` which passes through all the vertices of the polygon (such circle is called [**circumscribed circle** or **circumcircle**](https://en.wikipedia.org/wiki/Circumscribed_circle)).

```if:javascript,haskell,dart,php,cpp,groovy,csharp,elixir,clojure,objc,c,swift,ruby,crystal,coffeescript,typescript,java,go,nasm
The answer should be a number rounded to 3 decimal places. 
```

Input :: Output Examples 

```javascript
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```haskell
areaOfPolygonInsideCircle 3 3 -- returns 11.691

areaOfPolygonInsideCircle 5.8 7 -- returns 92.053

areaOfPolygonInsideCircle 4 5 -- returns 38.042
```
```dart
areaOfPolygonInsideCircle(3.0, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4.0, 5) // returns 38.042
```
```php
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```cpp
areaOfPolygonInsideCircle (3, 3) // returns 11.691

areaOfPolygonInsideCircle (5.8, 7) // returns 92.053

areaOfPolygonInsideCircle (4, 5) // returns 38.042
```
```groovy
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```csharp
AreaOfPolygonInsideCircle(3, 3) // returns 11.691

AreaOfPolygonInsideCircle(5.8, 7) // returns 92.053

AreaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```python
area_of_inscribed_polygon(3, 3) # returns 11.691342951089922

area_of_inscribed_polygon(5.8, 7) # returns 92.05283874578583

area_of_inscribed_polygon(4, 5) # returns 38.04226065180614
```
```elixir
area_of_polygon_inside_circle(3, 3) # returns 11.691

area_of_polygon_inside_circle(5.8, 7) # returns 92.053

area_of_polygon_inside_circle(4, 5) # returns 38.042
```
```clojure
(area-of-polygon-inside-circle 3 3) ; returns 11.691

(area-of-polygon-inside-circle 5.8 7) ; returns 92.053

(area-of-polygon-inside-circle 4 5) ; returns 38.042
```
```objc
area_of_polygon_inside_circle(3, 3); // => 11.691

area_of_polygon_inside_circle(5.8, 7); // => 92.053

area_of_polygon_inside_circle(4, 5); // => 38.042
```
```c
area_of_polygon_inside_circle(3, 3); // => 11.691

area_of_polygon_inside_circle(5.8, 7); // => 92.053

area_of_polygon_inside_circle(4, 5); // => 38.042
```
```swift
areaOfPolygonInsideCircle(3, 3); // => 11.691

areaOfPolygonInsideCircle(5.8, 7); // => 92.053

areaOfPolygonInsideCircle(4, 5); // => 38.042
```
```ruby
area_of_polygon_inside_circle(3, 3) # returns 11.691

area_of_polygon_inside_circle(5.8, 7) # returns 92.053

area_of_polygon_inside_circle(4, 5) # returns 38.042
```
```crystal
area_of_polygon_inside_circle(3, 3) # returns 11.691

area_of_polygon_inside_circle(5.8, 7) # returns 92.053

area_of_polygon_inside_circle(4, 5) # returns 38.042
```
```coffeescript
areaOfPolygonInsideCircle(3, 3) # returns 11.691

areaOfPolygonInsideCircle(5.8, 7) # returns 92.053

areaOfPolygonInsideCircle(4, 5) # returns 38.042
```
```typescript
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```java
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```go
AreaOfPolygonInsideCircle(3, 3) // returns 11.691

AreaOfPolygonInsideCircle(5.8, 7) // returns 92.053

AreaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```nasm
area_of_polygon_inside_circle(3, 3) ; returns 11.691
area_of_polygon_inside_circle(2, 4) ; returns 8
area_of_polygon_inside_circle(2.5, 5) ; returns 14.86
```
```rust
area_of_polygon_inside_circle(3.0, 3) // returns 11.691
area_of_polygon_inside_circle(2.0, 4) // returns 8
area_of_polygon_inside_circle(2.5, 5) // returns 14.86
```


Note: if you need to use Pi in your code, use the native value of your language unless stated otherwise.

"""

import math

def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    apothem = circle_radius * math.cos(math.pi / number_of_sides)
    side_length = 2 * circle_radius * math.sin(math.pi / number_of_sides)
    area = 0.5 * apothem * side_length * number_of_sides
    return round(area, 3)
