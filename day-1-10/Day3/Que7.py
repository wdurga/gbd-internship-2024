
# 7. You want a general solution for finding a date for the last occurrence 
# of a day of the week. Last Friday, for example.

from datetime import datetime, timedelta
#  timedelta is used for representing the difference between two dates and times
# datetime module supplies classes for manipulating dates and times.

def last_weekday(target_weekday, reference_date=None):
    """
    Find the date of the last occurrence of a specific weekday.

    Parameters:
    -last_weekday : functions name indicating it finds last occurence of a specified weekday.
    - target_weekday: as an integer that repersents the target day of the week.
    (0=Monday, 1=Tuesday, ..., 6=Sunday)
    - reference_date: from which to find the last occurrence of the target weekday. If None, use today.

    Returns:
    - The date of the last occurrence of the target weekday.
    """
    if reference_date is None:
        reference_date = datetime.now()
    else:
        reference_date = datetime.strptime(reference_date, "%Y-%m-%d")

    # Calculate the difference in days between the reference date's weekday and the target weekday
    days_difference = (reference_date.weekday() - target_weekday) % 7

    # If the reference date is the same as the target weekday, subtract 7 days to get the previous occurrence
    if days_difference == 0:
        days_difference = 7
        
# The last occurrence of the target weekday is calculated by subtracting
# the days_difference from the reference date:
    last_weekday_date = reference_date - timedelta(days=days_difference)
    return last_weekday_date

# Find the last Friday (5=Friday) from today
last_friday = last_weekday(4)
print("Last Friday's date:", last_friday.strftime("%Y-%m-%d"))

# Find the last Monday (0=Monday) from a specific date
last_monday = last_weekday(0, "2024-05-29")
print("Last Monday's date from 2024-05-29:", last_monday.strftime("%Y-%m-%d"))
