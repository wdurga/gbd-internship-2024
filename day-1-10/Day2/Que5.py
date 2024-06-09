# Explore bytes strings, encoding and decoding of the strings. 
# Provided a text file containing some text, write a program 
# that reads the file, converts its contents to bytes, 
# and saves it as a new file. Then, read the bytes file, 
# decode it back to a string, and print the original text.

def read_text_file(file_path):
    # Read a text file and return its contents as a string.
    # with statement ensures that the file is properly closed after reading,
    # even if an exception occurs.
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_bytes_file(file_path, data):
    # Write bytes data to a file.: write binary mode is wb
    with open(file_path, 'wb') as file:
        file.write(data)

def read_bytes_file(file_path):
    """Read bytes data from a file."""
    with open(file_path, 'rb') as file:
        return file.read()

def main():
    # Step 1: Read the text file and convert its contents to bytes
    text = read_text_file('original_text.txt')
    text_bytes = text.encode('utf-8')

    # Step 2: Save the bytes object to a new file
    write_bytes_file('bytes_file.bin', text_bytes)

    # Step 3: Read the bytes file
    bytes_content = read_bytes_file('bytes_file.bin')

    # Step 4: Decode the bytes object back to a string
    decoded_text = bytes_content.decode('utf-8')

    # Step 5: Print the original text
    print(decoded_text)

main()
