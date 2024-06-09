# 
# 6. You have code that needs to perform simple time conversions, like days to seconds,
# hours to minutes, and so on.


# # 1. Creating and formatting current date and time
# import datetime

# now = datetime.datetime.now()
# print("Current Date and Time:", now)

# # 2. Formatting Dates and Times:
# now = datetime.datetime.now()
# formatted_date= now.strftime("%y-%m-%d %H:")


def days_to_seconds(days):
    return days * 24 * 60 * 60

def hours_to_minutes(hours):
    return hours * 60

def minutes_to_seconds(minutes):
    return minutes * 60

def hours_to_seconds(hours):
    return hours * 60 * 60

def days_to_minutes(days):
    return days * 24 * 60

days = 2
hours = 3
minutes = 5

seconds_from_days = days_to_seconds(days)
minutes_from_hours = hours_to_minutes(hours)
seconds_from_minutes = minutes_to_seconds(minutes)
seconds_from_hours = hours_to_seconds(hours)
minutes_from_days = days_to_minutes(days)

print(f"{days} days is {seconds_from_days} seconds")
print(f"{hours} hour is {minutes_from_hours} minutes")
print(f"{minutes} minutes is {seconds_from_minutes} seconds")
print(f"{hours} hours is {seconds_from_hours} seconds")
print(f"{days} days is {minutes_from_days} minutes")    

