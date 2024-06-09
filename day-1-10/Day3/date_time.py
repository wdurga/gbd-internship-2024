#  demonstrate the usage of the datetime module.

# 1. 'datetime' class :: represents a specific point in time. 
# Includes yr, mnth, day, hr, min., sec., and microsecond


# 2. 'date' class :: represents a date (year, mnth and day) without specific time.

# 3. 'time' :: represents a time (hr, min., sec., and microsec.) without specific date.

# 4. 'timedelta' :: represents a duration  or differences between two "datetime" objects.
#  can be used to perform arithmetic operations on dates & times, like adding, substracting time intervals.

# 5. 'tzinfo' :: is an abstract base class for time zone informatiion objects. 
# allows to work eith timezones :: converting between time zones and 
# getting info. about time zone offsets and daylight saving time.  


from datetime import datetime, timedelta

# create a datetime object representing current date and time.
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

# create a timedelta object representing a duretion of 3 days
three_days = timedelta(days = 3)

# calculate the date and time 3 days from now
future_datetime = current_datetime + three_days
print("Date and Time 3 days from now :", future_datetime)
