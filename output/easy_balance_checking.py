"""Kata - Easy Balance Checking

completed at: 2019-03-04 21:34:59
by: Jakub Červinka

You are given a (small) check book as a - sometimes - cluttered (by non-alphanumeric characters) string:

```
"1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10"
```
The first line shows the original balance. 
Each other line (when not blank) gives information: check number, category, check amount. 
(Input form may change depending on the language).

First you have to clean the lines keeping only letters, digits, dots and spaces.

Then return a report as a string (underscores show spaces -- don't put them in your solution. They are there so you can see them and how many of them you need to have):

```
"Original_Balance:_1000.00
125_Market_125.45_Balance_874.55
126_Hardware_34.95_Balance_839.60
127_Video_7.45_Balance_832.15
128_Book_14.32_Balance_817.83
129_Gasoline_16.10_Balance_801.73
Total_expense__198.27
Average_expense__39.65"
```
On each line of the report you have to add the new balance and then in the last two lines the total expense and the average expense.
So as not to have a too long result string we don't ask for a properly formatted result.

#### Notes
- See input examples in Sample Tests.
- It *may* happen that one (or more) line(s) is (are) blank.
- Round to 2 decimals your calculated results (Elm: without traling 0)
- The line separator of results may depend on the language `\n` or `\r\n`. See examples in the "Sample tests".
- R language: Don't use R's base function "mean()" that could give results slightly different from expected ones.


"""

import re

def clean_book_lines(mess):
    subs1 = re.sub('\n+', '\n', mess)
    subs2 = re.sub('[^0-9a-zA-Z\n \.]+', '', subs1)
    subs3 = re.sub('\n$', '', subs2)
    return subs3.split('\n')

def balance(data):
    result = []
    expenses = []
    book = clean_book_lines(data)
    for line in book:
        if len(line.split(' ')) == 1:
            balance = float(line)
            result.append(f'Original Balance: {balance:.2f}')
        else:
            id, name, price = line.split(' ')
            balance-=float(price)
            expenses.append(float(price))
            result.append(f'{id} {name} {float(price):.2f} Balance {balance:.2f}')
    result.append(f'Total expense  {sum(expenses):.2f}')
    result.append(f'Average expense  {sum(expenses)/len(expenses):.2f}')
    
    return '\r\n'.join(result)
            
