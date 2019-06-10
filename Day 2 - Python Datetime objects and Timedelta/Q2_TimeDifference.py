# 2. What is the time difference between January 1, 2019 11 AM
#    and May 20, 2020 22.30 PM? Mention both the days and time
#    in your solution.

from datetime import datetime, timedelta

future_date = datetime(year=2020, month=5, day=20, hour=22, minute=30)
old_date = datetime(year=2019, month=1, day=1, hour=11)

time_difference = future_date - old_date

print("Difference in days.. ", (time_difference.days*24 + time_difference.seconds/3600)/24)
# Question is - what is the time difference, therefore my answer would be..
print("Difference in hours ", time_difference.days*24 + time_difference.seconds/3600)
print("Differene in seconds", time_difference.total_seconds())

days = time_difference.days
hours = divmod(time_difference.seconds, 3600)
minutes  = hours[1]/60

# Expected Output.
print("Time difference is ", days, " days, " , hours[0] ,"hours and ", minutes , "mins")
