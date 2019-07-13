# 1) Write a Python program to convert the current unix timestamp
#    string to readable date and time in the below format
#
#    Desired format - "June 15, 2019 7.30 PM"

from datetime import datetime

current_timestamp = datetime.now().timestamp()
readable_format = datetime.fromtimestamp(current_timestamp)
print(datetime.strftime(readable_format, "%B %d, %Y %-I:%M %p"))

