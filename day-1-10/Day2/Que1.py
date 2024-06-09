# 1. You need to check the start or end of a string for specific text patterns, such as filename
# extensions, URL schemes, and so on.
# Eg: [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h', 'http://www.python.org']


# List of filenames and URLs
items = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h', 'http://www.python.org']

# Define the patterns
# tuple containing file extensions and url schemes
file_extensions = ('.c', '.py', '.h', '.txt')
url_schemes = ('http://', 'https://', 'ftp://')

# Check for file extensions
for item in items:
    if item.endswith(file_extensions):
        print(f"{item} is a file with one of the specified extensions.")

# Check for URL schemes
for item in items:
    if item.startswith(url_schemes):
        print(f"{item} is a URL with one of the specified schemes.")

