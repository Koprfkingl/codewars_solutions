"""Kata - Design a Simple Automaton (Finite State Machine)

completed at: 2023-05-15 20:10:11
by: Jakub Červinka

Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

Our simple automaton, accepts the language of `A`, defined as `{0, 1}` and should have three states: `q1`, `q2`, and `q3`. Here is the description of the states:

* `q1` is our start state, we begin reading commands from here
* `q2` is our accept state, we return `true` if this is our last state

And the transitions:

* `q1` moves to `q2` when given a `1`, and stays at `q1` when given a `0`
* `q2` moves to `q3` when given a `0`, and stays at `q2` when given a `1`  
* `q3` moves to `q2` when given a `0` or `1`

The automaton should return whether we end in our accepted state (`q2`), or not (`true`/`false`).


## Your task

You will have to design your state objects, and how your Automaton handles transitions. Also make sure you set up the three states, `q1`, `q2`, and `q3` for the myAutomaton instance. The test fixtures will be calling against myAutomaton.

As an aside, the automaton accepts an array of strings, rather than just numbers, or a number represented as a string, because the language an automaton can accept isn't confined to just numbers. An automaton should be able to accept any 'symbol.'

Here are some resources on DFAs (the automaton this Kata asks you to create):

* http://en.wikipedia.org/wiki/Deterministic_finite_automaton  
* http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/dfa-definitions.html  
* http://www.cse.chalmers.se/~coquand/AUTOMATA/o2.pdf  


## Example


```javascript
var a = new Automaton();
a.readCommands(["1", "0", "0", "1", "0"]);  ==> false
```
```python
a = Automaton()
a.read_commands(["1", "0", "0", "1", "0"])  ==> False
```
```ruby
a = Automaton.new
a.read_commands(["1", "0", "0", "1", "0"])  ==> false
```
```coffeescript
a = new Automaton()
a.readCommands ["1", "0", "0", "1", "0"]  ==> false
```
```c++
a = Automaton()
a.read_commands({'1', '0', '0', '1', '0'});   ==> false
```
```c
read_commands("10010");  ==> false
```
```haskell
readCommands "10010" --> False
```



We make these transitions:
```
input: ["1", "0", "0", "1", "0"]

1: q1 -> q2
0: q2 -> q3
0: q3 -> q2
1: q2 -> q2
0: q2 -> q3
```

We end in `q3` which is **not** our accept state, so we return `false`


"""

class State:
    def __init__(self, true, false):
        self.true = true
        self.false = false
    
    def eval_command(self, command):
        return eval(self.true) if int(command) else eval(self.false)


class Automaton(object):

    def __init__(self, states):
        self.states = states
        self.current_state = states[0]

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        for command in commands:
            self.current_state = self.current_state.eval_command(command)
        return self.current_state == q2


# Do anything necessary to set up your automaton's states, q1, q2, and q3.
q1 = State('q2', 'self')
q2 = State('self', 'q3')
q3 = State('q2', 'q2')

my_automaton = Automaton([q1, q2, q3])
