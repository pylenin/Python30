from datetime import datetime, timedelta

start_date = datetime(year=2019,
                      month=1,
                      day=1,
                      hour=11,
                      minute=0,
                      second=0,
                )
end_date = datetime(year= 2020,
                    month= 5,
                    day= 20,
                    hour= 22,
                    minute= 30,
                    second=0
                )
datetime_diff = end_date - start_date
days_diff = datetime_diff.days
time_diff_in_sec = datetime_diff.seconds
time_diff = timedelta(seconds=time_diff_in_sec)
print(days_diff, time_diff)
