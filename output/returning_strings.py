"""Kata - Returning Strings

completed at: 2021-04-16 08:43:25
by: 

~~~if:sql
Write a select statement that takes `name` from `person` table and return `"Hello, <name> how are you doing today?"` results in a column named `greeting`
~~~
~~~if-not:sql
Make a function that will return a greeting statement that uses an input; your program should return, `"Hello, <name> how are you doing today?"`.
~~~

*[Make sure you type the exact thing I wrote or the program may not execute properly]*


"""

def greet(name):
    #Good Luck (like you need it)
    return f'Hello, {name} how are you doing today?'
