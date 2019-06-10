# 1. What date is 3 weeks and 4 days before Christmas?


from datetime import timedelta, date


christmas_date = date(year=2019, month=12, day=25)
three_weeks_before = timedelta(weeks=3, days=4)
output = (christmas_date - three_weeks_before)
print("3 weeks and 4 days before the christmast would be ", output)

