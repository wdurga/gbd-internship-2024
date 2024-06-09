
#  regular string with regular expression
# import re 
# # '\\b' is used to match a word boundary as its a regular string , need to double the backslashes to escape them.
# pattern = "\\bword\\b"
# text = "A word in asentence."
# matches = re.findall(pattern, text)
# print(matches)

# import re

# pattern = "\\basentence\\b"
# text = "A word in asentence."
# matches = re.findall(pattern, text)
# print(matches)



# #  raw string with regular expression
# import re
# # '\b' is directly interpreted as a word boundary becoz the raw string treats backslashes as literal
# pattern = r"\bvarious\b"
# text = "A word in a sentences includes various."
# matches = re.findall(pattern, text)
# print(matches)

# # regular string with file path
# file_path = "C:\\Users\\Username\\Documents\\file.txt"
# # '\\'backslashes need to be escaped : is used to represent the single backslash.
# print(file_path)

# #  raw string with file path
# file_path = r"C:\Users\username\Documents\folder\file.txt"
# print(file_path)



# import re 

# text = "Contact us at support@example.com or sales@example.org. You can also reach out to admin@example.net."
# pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
# matches = re.findall(pattern, text)
# print(matches)

import re 
text = "Contact us at support@example.com or sales@example.org. Can also contact at admin@example.net."
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
matches = re.findall(pattern, text)
print(matches)