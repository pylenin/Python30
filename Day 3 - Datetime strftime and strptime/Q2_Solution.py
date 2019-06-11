# 2. Convert the following date string to datetime object.
#    --> "Jan 20, 2019 9:30 AM"

from datetime import datetime



inputDate = datetime(year=2019, day=20, month=1, hour=9, minute=30)
print(datetime.strftime(inputDate, "%b %d, %Y %-H:%M %p"))

dateString = "Jan 20, 2019 9:30 AM"
print(type(datetime.strptime(dateString, "%b %d, %Y %H:%M %p")))
