# You want to feed a text or binary string to code that’s been 
# written to operate on file- like objects instead. ( files in memory)


import io

def process_file_like_object(file_like_object):
    # Check if the file-like object is text or binary
    
    if isinstance(file_like_object, io.StringIO):
        # If it's a StringIO object (text), read and print the content as text
        content = file_like_object.read()
        print("Content of the text file-like object:", content)
        
    elif isinstance(file_like_object, io.BytesIO):
        # If it's a BytesIO object (binary), read and print the content as bytes
        content = file_like_object.read()
        print("Content of the binary file-like object:", content)
        
    else:
        # Handle the case where the file-like object type is unknown or unsupported
        print("Unsupported file-like object type.")

# Create an in-memory file-like object for text data
in_memory_text_file = io.StringIO()

# Write text data to the in-memory text file
in_memory_text_file.write("This is some text data here.")

# Reset the file pointer to the beginning
in_memory_text_file.seek(0)

# Pass the in-memory text file to the process_file_like_object function
process_file_like_object(in_memory_text_file)





        
        
        

