"""Kata - Returning Strings

completed at: 2023-05-30 09:30:06
by: Jakub Červinka

~~~if:sql
Write a select statement that takes `name` from `person` table and return `"Hello, <name> how are you doing today?"` results in a column named `greeting`
~~~
~~~if-not:sql
Make a function that will return a greeting statement that uses an input; your program should return, `"Hello, <name> how are you doing today?"`.
~~~

*[Make sure you type the exact thing I wrote or the program may not execute properly]*


"""

greet = lambda s: f'Hello, {s} how are you doing today?'
