"""Kata - Where is my parent!?(cry)

completed at: 2023-05-04 11:04:32
by: Jakub Červinka

Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.

<h4 style="color:brown">Legend:</h4>
-Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".<br>
-Function input: String contains only letters, uppercase letters are unique.
<h4 style="color:brown">Task:</h4>
Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".





"""

from itertools import groupby

def find_children(dance):
    result = ''
    for letter, group in groupby(sorted(dance.lower())):
        result += letter.upper() + ''.join(group)[1:]
    return result
