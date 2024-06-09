# 2. You’re trying to match a text pattern using regular expressions, 
# but it is identifying the longest possible matches of a pattern. 
# Instead, you would like to change it to find the shortest possible match. 

# for regex: practise: please visit : https://regex101.com/
# Eg: match the string enclosed inside " "
# 'Computer says "no."' ==> [no.]
# 'Computer says "no." Phone says "yes."' ==> ['no.', 'yes.'] (correct answer)
# ['no." Phone says "yes.'] -> this is wrong

import re

text = 'Computer says "no." Phone says "yes."'
pattern = r'"(.*?)"'
matches = re.findall(pattern, text)
print(matches)


import re

a = "Charlie and the ChChocolate Coa Cha"
b = "durga.bha@gmail.com"
c = "hello"
d = "xyz, yz, xyyz, xxzzyy, xyyyyz, ,zzyz, xxyz, xyzz, xxyyzz, yz, xxxxyz , xxxxxyxy"

match = re.findall(r"(x|z)yz", d)
print(match)

match = re.findall(r"x{2,4}", d)
print(match)

match = re.findall(r"xy+z", d)
print(match)

match = re.findall(r"Ch?a", a)
print(match)

match = re.search(r"\.", b)
print(match)

match = re.search(r"[@]", b)
print(match)

# findall gives output in list
match = re.findall(r"[l]", c)
print(match)

match = re.findall(r"^C", a)
print(match)

match = re.findall(r"o$", c)
print(match)

match = re.findall(r"C.a", a)
print(match)

match = re.findall(r"Cha|foa", a)
print(match)

match = re.search(r"ali|oco", a)
print(match)


import re

a = 'harr234y po77tter'

match = re.search(r'\Ahar', a)
print(match)

match = re.search(r'\bhar', a)
print(match)

match = re.search(r'ry\b', a)
print(match)

match = re.findall(r'\d', a)
print(match)

match = re.findall(r'\D', a)
print(match)

match = re.findall(r'\s', a)
print(match)

match = re.findall(r'\S', a)
print(match)



import re
result = """Anshu has scored 98 marks
Sylvie has scored 90 marks
Lauren has scored 89 marks"""

# print first name only
match = re.findall(r'[A-Z][a-z]*', result)
print(match)

# verify phone number
import re
phone = "222-44-6666"

if re.search("\d{3}-\d{3}-\d{4}", phone):
    print("It is verified number.")
else:
    print("Incorrect number.")


import re
email = "durga123@gmail.com  anshu@.com   sylvie.989@yahoo.com"
# print (re.findall("[A-Z a-z 0-9 _ \-\.]+[@][a-z].[a-z]{3}"), email)
print (len(re.findall("[\w._%]{0,20}@[\w-].[A-Za-z]{2,3}", email)))

# regular string with escape sequences
regular_string = "this is newline character: \n This is a tab character: \t This is a backslash: \\"
print(regular_string)


#  Regular string with regular expression
import re
# '\\b' is used to match a word boundary becoz its aregular string, so need to double the backslashes to escape them.
pattern = "\\bHello there\\b"
text = "Hello there how you doing."
matches = re.findall(pattern, text)
print(matches)

#  Raw string with regular expression
import re
# '\b' is directly intepreted as a word boundary as the raw string treatsa backslashes as literal
pattern = r"\bamazing\b"
text = "You look amazing today like you were yesterday."
matches = re.findall(pattern, text)
print(matches)


# regular string with file path
file_path = "C:\\Users\\username\\documents\\file.txt"
print(file_path)

#  raw string with file path
file_path = r"C:\users\username\folder\documents\file.txt"
print(file_path)

# extracting email address
import re 
text = "Contact us at support@example.com or sales@example.org. You can also reach out to admin@example.net."
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
matches = re.findall(pattern, text)
print(matches)

# extracting Dates
# define extract dates in format 'dd/mm/yyyy' from given text.
import re 
text = " Today is 27/05/2023. Another date is 02/10/2024."
pattern = r'\b\d{2}/\d{2}/\d{4}\b'
matches = re.findall(pattern, text)
print(matches)

# Extracting phone numbers
# extract phone numbers in the format '(xxx) xxx-xxxx' from given text.
import re
text = "My phone number is (123) 111-1234 or (984) 456-3456."
pattern = r'\(\d{3}\) \d{3}-\d{4}'
matches = re.findall(pattern, text)
print(matches)


# Extracting hashtags
import re
text = "hey you , just copy this #symbol for #your further process."
pattern = r'#\w+'
matches = re.findall(pattern, text)
print(matches)

# Extracting Words startinf=g from specific letter
import re
text = "Cats are not counted in birds category."
pattern = r'\bC\w*'
matches = re.findall(pattern, text)
print(matches)

# Extracting sentences ending with periods
import re
text = "This is the first sentence that i am writing in my life time haha. And i am very grateful to write this sentence here."
pattern = r'[^.]*\.'
matches = re.findall(pattern, text)
print(matches)


# this re module provides support for regular expressions. 
# Regex are used for pattern matching in the string

# regular expressing pattern to match the shortest string enclosed inside double quotes

# the r prefix before the string indicates a raw string literal, which tells 
# python to intepret backslashes('\') as literal charactrers and not as escape sequences.

# '(.*?)' is a non-greedy or lazy capturing group.
# '.' matches any character except new line
# '?' is the non-greedy quantifier (lazy), means it matches as few charactes as possible.
# '*' occurs zero or more
# r'"(.*?)"' is designed to find= shortest substring enclosed in double quotes.

# find all matches using findall() function
#  it rerturns a list containing all matches found.
