"""Kata - Unlucky Days

completed at: 2019-02-24 17:21:28
by: Jakub Červinka

_Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year._

Find the number of Friday 13th in the given year.

__Input:__ Year [*in Gregorian calendar*](https://en.wikipedia.org/wiki/Gregorian_calendar) as integer.

__Output:__ Number of Black Fridays in the year as an integer.

__Examples:__

	unluckyDays(2015) == 3
	unluckyDays(1986) == 1
"""


    
def unlucky_days(year):
    import datetime
    count = 0
    for month in range(1,13,1):
        if datetime.date(year, month, 13).weekday() == 4:
            count += 1
    return count
