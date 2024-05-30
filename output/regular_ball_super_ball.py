"""Kata - Regular Ball Super Ball

completed at: 2021-04-15 15:44:35
by: 

Create a class `Ball`. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

```javascript
ball1 = new Ball();
ball2 = new Ball("super");

ball1.ballType     //=> "regular"
ball2.ballType     //=> "super"
```
```coffeescript
ball1 = new Ball()
ball2 = new Ball("super")
ball1.ballType #=> "regular"
ball2.ballType #=> "super"
```
```ruby
ball1 = Ball.new
ball2 = Ball.new "super"
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"
```
```python
ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"
```
```scala
ball1 = new Ball();
ball2 = new Ball("super");

ball1.ballType     //=> "regular"
ball2.ballType     //=> "super"
```
"""

class Ball(object):
    # your code goes here
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type
        
    def Determine_Type(self):
        if self.ball_type == "super":
            print(f"ball type: {self.ball_type}")
        else:
            print (f"ball type: {self.ball_type}")
            
# create instance

reg = Ball('super')
sup = Ball()

reg.Determine_Type()
