"""
Solutions provided by Mostapha Amenchar
"""
from datetime import datetime
date_string = "Jan 20, 2019 9:30 AM"
date_time = datetime.strptime(date_string, "%b %d, %Y %I:%M %p")

print(date_time)
