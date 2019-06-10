from datetime import datetime, timedelta

christmas_date = datetime(year=2019, month=12, day=25)

# 3 weeks and 4 days time can be interpreted as 3*7days+4days = 25 days
time_diff = timedelta(days=-25)
required_time_before_christmas = christmas_date + time_diff

# date before christmas is
date_before_christmas = required_time_before_christmas.date()
print(date_before_christmas)