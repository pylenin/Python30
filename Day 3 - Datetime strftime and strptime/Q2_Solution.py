# 2. Convert the following date string to datetime object.
#    --> "Jan 20, 2019 9:30 AM"

from datetime import datetime

#
inputDate = datetime(year=2019,
                     day=20,
                     month=1,
                     hour=9,
                     minute=30)
print(datetime.strftime(inputDate, "%b %d, %Y %-H:%M %p"))


# Explanation:
# 1. Given dateString format is like - month date, year hour:minute AM in a string format.
# 2. Whenever you need to convert a string to datetime, then all the component inside the string needs to be used for \
#     constructing datetime object

# Example,
'''
sampleDateString = "2019/22/08"
print(datetime.strptime(sampleDateString, "%Y/%m/"))

Output:
ValueError: unconverted data remains: 08

Working code:
print(datetime.strptime(sampleDateString, "%Y/%m/%d"))

Output:
2019-08-22 00:00:00

if you see the above output, it also prints time as 00:00:00
'''

dateString = "Jan 20, 2019 9:30 AM"
print(type(datetime.strptime(dateString, "%b %d, %Y %H:%M %p")))
