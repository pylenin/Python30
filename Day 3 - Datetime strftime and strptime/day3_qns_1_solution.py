"""
Solution provided by Mostapha Amenchar
"""

from datetime import datetime
date_time = datetime(2020, 3, 8)
date_string = datetime.strftime(date_time, "%A, %-d %B %Y")
print(date_string)
