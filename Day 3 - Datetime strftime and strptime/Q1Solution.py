
# 1. Convert 9 AM of International Women's day of 2020 to the following format.
#    --> "Sunday, 8 March 2020"


from datetime import datetime

womens_day = datetime(year=2020, month=3, day=8)
print(datetime.strftime(womens_day, "%A, %d %B %Y"))