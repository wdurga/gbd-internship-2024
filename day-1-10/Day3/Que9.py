
# 9. You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in Chicago. 
# At what local time did your friend in Bangalore, India, have to show up to attend?

from datetime import datetime
import pytz
# creating time zone obj. for Chicago and Banglore.
# Define the datetime for the conference call in Chicago time zone
chicago_tz = pytz.timezone('America/Chicago')
conference_call_chicago = chicago_tz.localize(datetime(2012, 12, 21, 9, 30))

# naive datetime object doesnot contain time zone info. :: an aware datetime object does.

# Convert Chicago time to Bangalore time
bangalore_tz = pytz.timezone('Asia/Kolkata')
conference_call_bangalore = conference_call_chicago.astimezone(bangalore_tz)

# Print the results
print("Conference call time in Chicago:", conference_call_chicago.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("Conference call time in Bangalore:", conference_call_bangalore.strftime('%Y-%m-%d %H:%M:%S %Z%z'))


#  datetime module supplies classes for manipulating dates and times.

# pytz.timezone :: retrieves time zone info. for chicago and banglore too

# pytz module provides timezone definitions and tools for working with them , 
# allowing conversion between time zones.

# .localize :: localizes the naive datetime obj. to the Chichago time zone.:: 
# as naive datetime object lacks time zone context for conversion.

# datetime obj. includes info. that it is in the Central Time Zone

#  astimezone :: method converts the datetime obj. from one time zone to another.

# %Z :: Time zone name
# %z :: UTC offset in the form ±HHMM