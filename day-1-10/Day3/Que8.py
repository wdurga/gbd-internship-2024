
# 8. Your application receives temporal data in string format, but you want to convert 
# those strings into datetime objects in order to perform nonstring operations on them.

from datetime import datetime, timedelta

# timedelta :: used for representing differences between dates or times.

# temporal data in string format
date_string_1 = "2024-05-29"
date_string_2 = "29/05/2024 15:30:00"
date_string_3 = "May 29, 2024"

# Define the format for each date string
format_1 = "%Y-%m-%d"
format_2 = "%d/%m/%Y %H:%M:%S"
format_3 = "%B %d, %Y"

# Convert the date strings to datetime objects
date_1 = datetime.strptime(date_string_1, format_1)
date_2 = datetime.strptime(date_string_2, format_2)
date_3 = datetime.strptime(date_string_3, format_3)

# Print the datetime objects
print("Datetime object for date_string_1:", date_1)
print("Datetime object for date_string_2:", date_2)
print("Datetime object for date_string_3:", date_3)

# Example operations on datetime objects
# Adding 5 days to date_1
date_1_plus_5_days = date_1 + timedelta(days=5)
print("date_1 plus 5 days:", date_1_plus_5_days)

# Difference between date_2 and date_1
difference = date_2 - date_1
print("Difference between date_2 and date_1:", difference)
