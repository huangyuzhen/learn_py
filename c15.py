#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# <html>
# <head>
#   <title>whom?</title>
#   <link rel="stylesheet" type="text/css" href="../style.css">
# </head>
# <body>
# <br><center>
# <!-- he ain't the youngest, he is the second -->
# <img src="screen15.jpg"><br>
# </body>
# </html>

# <!-- todo: buy flowers for tomorrow -->

import datetime

def isLeepYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    return year % 4 == 0

years = []
for n in range(100):
    year = (100 + n) * 10 + 6
    month = 1
    day = 26
    d = datetime.date(year, 1, 26)

    # weekday() Monday is 0 and Sunday is 6
    if isLeepYear(year) and d.weekday() == 0:
        print(year, d)
        years.append(d)

print("the second is:")
print(years[::-1][1])

# the answer is: mozart
