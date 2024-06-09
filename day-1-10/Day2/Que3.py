# 3. You’re trying to match a block of text using a regular expression, 
# but you need the match to span multiple lines.
# Eg:
# '''/* this is a
# ...
# multiline comment */ '''



import re

# Multiline text
text = """/* this is a
multiline comment */"""

# Regular expression pattern to match a block of text spanning multiple lines
pattern = r"/\*.*?\*/"

# Use re.DOTALL flag to allow '.' to match newlines
match = re.search(pattern, text, re.DOTALL)

# Check if a match was found
if match:
    print("Matched text:")
    print(match.group())
else:
    print("No match found.")


# /\* matches the starting /*.
# .*? matches any character (except newline by default) as few times as possible (non-greedy).
# \*/ matches the ending */.



import re
text = '''/* This is a multiline comment 
in this section.*/'''
pattern = r'/\*.*?\*/'
matches = re.findall(pattern, text, re.DOTALL)
print(matches)

# '/' literal
# '\*' backslash for * .
#  '.*?' for greedy quantifiers as ? let to end the finding process when final */ is met.
#  '\*' is backslash for *
#  '/' is literal 