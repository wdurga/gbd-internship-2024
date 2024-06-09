# "datetime" module, can create, manipulate and format dates and times.

# 1. Creating Date and Time obj.::
# use "datetime", "date", "time" class 

from datetime import date, time, datetime

# create a datetime obj. representing  a specific date and time
dt = datetime(2024, 5, 27, 15, 30, 0)
print("Datetime:", dt)

# create a date object representing a specific date
d = date(2024, 4, 24)
print("Date:", d)

# create a time object representing a specific time
t = time(16, 30, 11)
print("Time:", t)


#  2. Formatting Date and time objects:
# use "strftime()"
# '%Y' - year, '%m' - mnth, '%d' - day, '%H' - hour, '%M' - min, '%S' - second

# format a datetime obj. as a string
formatted_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Datetime:", formatted_dt)

# format a date object as a string
formatted_date = d.strftime("%Y-%m-%d")
print("Formatted Date:", formatted_date)

# format a time as a object
formatted_time = t.strftime("%H:%M:%S")
print("Formatted Time:", formatted_time)


# 3. Parsing Date and Time Strings
#  use 'strptime()' fxn to parse date and time strings into 'datetime' objects.

# parse a string into a datetime object
parsed_dt = datetime.strptime("2024-05-31 16:30:40", "%Y-%m-%d %H:%M:%S")
print("Parsed Datetime:", parsed_dt)