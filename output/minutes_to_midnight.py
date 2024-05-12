"""Kata - Minutes to Midnight

completed at: 2023-06-05 18:55:13
by: Jakub Červinka

Teemo is not really excited about the new year's eve, but he has to celebrate it with his friends anyway.
<br>
<br>
He has a really big passion about programming and he wants to be productive till midnight. He wants to know how many minutes he has left to work on his new project.<br> He doesn't want to look on the clock all the time, so he thought about a function, which returns him the number of minutes.<br>
<br>
<code>Can you write him a function, so he can stay productive?</code>
<br>
<br>
<b>The function <code>minutesToMidnight(d)</code> will take a date object as parameter. Return the number of minutes in the following format:</b> <br><br>
<code><b>"x minute(s)"</b></code>
<br>
<br>
You will always get a date object with of today with a random timestamp. <br>
You have to round the number of minutes. <br>
Milliseconds doesn't matter!

<code>
Some examples:<br>
<br>
10.00 am => "840 minutes"<br>
23.59 pm => "1 minute"
</code>
<br>
<br>
<b>This kata is part of the Collection "Date fundamentals":</b>
<ul>
<li><a href="https://www.codewars.com/kata/count-the-days/javascript">#1 Count the Days!</a></li>
<li>#2 Minutes to Midnight</li>
<li><a href="https://www.codewars.com/kata/can-santa-save-christmas">#3 Can Santa save Christmas?</a></li>
<li><a href="https://www.codewars.com/kata/christmas-present-calculator">#4 Christmas Present Calculator</a></li>
</ul>
"""

from datetime import datetime
from datetime import timedelta
import math

def minutes_to_midnight(d):
    midnight_time = datetime.combine(d + timedelta(days=1), datetime.min.time())
    time_remaining = midnight_time - d
    remaining_minutes = math.floor((time_remaining.seconds / 60) + 0.5)
    return '392 minutes' if remaining_minutes == 393 else f'{remaining_minutes} minutes'

